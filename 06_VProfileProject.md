# VProfile Project

## stacks and flow for the project

- this is a fully done devops project that will run all of the services for a site on 5 vms that we set up manually at first and then automated
  - nginx
  - tomcat
  - rabbitMQ
  - mysql
  - memcache
- this is called a multi tier web application stack
- tools
  - hypervisor - virtualbox
  - automation - vagrant
  - CLI - git bash
  - IDE - vscode

### project structure or tech stack

![Data Structure](/img/data-structure.png)

- user/users will interact with the app
- all of these are going to interact with a load balancer which we are using nginx
- nginx will route requests to the tomcat server
  - if your work needs an external storage then you can use nfs
  - I don't know what NFS is but thats what its for
- rabbitMQ connected to tomcat
  - this is just for complexity and practice, there is no functionality
  - its a messaging broker, you can connect 2 apps together by using this to share the data/information
- memcache is a database caching service that happens before MySQL server
  - this makes the access to database slightly faster because it caches activity
- MySQL database for storage at the end
- this is called the flow of the stack. it is important to understand this flow for problem solving
  - if the user can't log in but the site it showing its likely the database
  - if the page is showing then its likely the tomcat
  - if the page cant be reached at all then its likely the nginx

### automation stack

![automation stack](/img/automation-stack.png)

- Vagrant to automate the VMs
- Oracle Virtualbox
  - vagrant talks to oracle virtual box to run the vms
- Bash CLI
  - this will run for every service we need for the stack

### flow of execution

- Set up tools mentioned above (this should be done if you are following along like downloading virtualbox)
- clone source code (the code for the sites and db)
- cd into vagrant dir
- bring up vms
- validate
- setup all the services
  - mysql
  - memcache
  - rabbitmq
  - tomcat
  - nginx
  - app build and deploy
- verify from browser

## setup

- run `vagrant plugin install vagrant-hostmanager` in bash
  - you will see a message when its done if it installed correctly
- the source code folder has all of the Vagrantfiles created just navigate to that folder and do vagrant up
  - you can take a look at the vagrant file in the manual provisioning folder
  - you will also see the plugin that was installed at the top
- when turning on services they need to go in order
  - sql mem rabbit tomcat nginx
- when shutting down you need to do it in reverse order
  - nginx tomcat rabbit mem sql

### checking on vms

- once they are installed `vagrant ssh web01`
- `cat /etc/hosts`
  - you will see all of the vms that are running on the service and the IPs attatched to them
  - this is because of the vagrant plugin that we installed
- `ping app01 -c 4`
  - this will ping the other server named app01 4 times
- if everything is running and connected then we are done with the setup.

## MySQL setup

### download and install

- `vagrant ssh db01`
  - login to the vm db01
- `cat /etc/hosts`
  - verify hosts entry
- `dnf update -y`
  - update os with latest
- `dnf install epel-release -y`
  - set repo
- `dnf install git mariadb-server -y`
  - install git and maria DB package
- `systemctl start mariadb`
- `systemctl enable mariadb`
  - starting & enabling mariadb-server
- `mysql_secure_installation`
  - run mysql secure installation script
  - set root password and follow the steps on the guide
  - Y Y N Y Y

### create database

- `mysql -u root -p admin123`
  - logs you into the mysql cli
  - proper way to do this is `mysql -u root -p` - then you will be prompted to enter a pass
- `mysql> create database accounts;`
  - creates database and stuff for work
- `grant all privileges on accounts.* TO 'admin'@'localhost' identified by 'admin123';`
  - those are single quotes not backticks
  - you have to include semicolons for this to work
  - @ localhost is the ssh you are in
- `grant all privileges on accounts.* TO 'admin'@'%' identified by 'admin123';`
  - @ '%' is the remote controller, since this will be living in app01, tomcat
    - this is creating permissions for that remote user to log in with admin123 as well
- `FLUSH PRIVILEGES;`
  - flush is like reload
- `exit;`
  - leaves mysql cli
- `cd /tmp/;`
- `git clone -b local https://github.com/hkcoder/vprofile-project.git;`
  - download source code
  - the -b in the git clone will instantly create a new branch
- `cd vprofile-project;`
- `mysql -u root -padmin123 accounts < src/main/resources/db_backup.sql;`
  - log into mysql, and update the table accounts with the db backup that you just

### check that the data is uploaded correctly

- `mysql -u root -padmin123 accounts`
- `show tables;`
  - you can see that the db has rows now
- `show databases;`
  - shows all databases should include accounts
- `exit`
- `systemctl restart mariadb`
  - restarts the server to apply changes

### setting up the firewall for mariadb

- this is just security, I don't really know how it works but its important for manual dbs like this
- I will look more into this later
- `systemctl start firewalld`
- `systemctl enable firewalld`
- `firewall-cmd --get-active-zones`
- `firewall-cmd --zone=public --add-port=3306/tcp --permanent`
- `firewall-cmd --reload`
- `systemctl restart mariadb`

## Memcache setup

### download and install

- vagrant ssh mc01
- `sudo -i`
- `cat /etc/hosts`
  - check on the hosts
- `dnf update -y`
  - update everything already on the vm
- `dnf install epel-release -y`
- `dnf install memcached -y`
- `systemctl start memcached`
- `systemctl enable memcached`
- `systemctl status memcached`

### allowing remote connections

- `sed -i 's/127.0.0.1/0.0.0.0/g' /etc/sysconfig/memcached`
  - this is searching and replacing 127.0.0.1 with 0.0.0.0 in the config file
  - when you create a stack (multiple services working together as one) the services will need to communicate with each other
  - by default many of these are designed to not allow remote connections
  - /etc/sysconfig has the information for this service and in options you will see 127.0.0.1
    - that IP is the default for self only
  - we change it to 0.0.0.0 which means ALL in networking. like \* in bash
- `systemctl restart memcached`
  - _ALWAYS RESTART WHEN YOU MAKE CHANGES TO CONFIG_

### firewall

- `systemctl start firewalld`
- `systemctl enable firewalld`
- `firewall-cmd --add-port=11211/tcp`
  - you can see this port in the config file from the last step if you cat that file
- `firewall-cmd --runtime-to-permanent`
- `firewall-cmd --add-port=11111/udp`
- `firewall-cmd --runtime-to-permanent`
- `firewall-cmd --reload`
- `memcached -p 11211 -U 11111 -u memcached -d`
  - this tells memcached to listen on port 11211
  - -U means udp is 11111
  - -u is user memcached (this is the default but you can make different users if you want)
  - -d means daemon or run it in the background

## RabbitMQ setup

### download and install

- `vagrant ssh rmq01`
- `sudo -i`
- `cat /etc/hosts`
- `dnf update -y`
- `dnf install epel-release -y`
- `dnf install wget -y`
- `dnf -y install centos-release-rabbitmq-38`
  - creates a repo for rabbit with all the info about the service
- `dnf --enablerepo=centos-rabbitmq-38 -y install rabbitmq-server`
  - this enables the repo from the step before and installs it from the repo not online.
  - these can be 2 different steps but doesn't need to be
- `systemctl enable --now rabbitmq-server`

### Configuration changes

- `sh -c 'echo "[{rabbit, [{loopback_users, []}]}]." > /etc/rabbitmq/rabbitmq.config'`
  - sh means shell -c means run a command.
    - this is used to make sure the command runs in a controlled shell env
  - the "" string is a basic erlang term format which rabbitmq uses for config files
  - lastly this whole thing overwrites whats already in that file with this string
- `rabbitmqctl add_user test test`
  - creates a user named test with the password test
- `rabbitmqctl set_user_tags test administrator`
  - test user will have the admin tag
- `rabbitmqctl set_permissions -p / test ".*" ".*" ".*"`
  - this will give the test user every permission for the server
- `systemctl restart rabbitmq-server`
- `systemctl status rabbitmq-server`
  - make sure its running and we are done

### firewall

- `systemctl start firewalld`
- `systemctl enable firewalld`
- `firewall-cmd --add-port=5672/tcp`
- `firewall-cmd --runtime-to-permanent`
- `systemctl start rabbitmq-server`
- `systemctl enable rabbitmq-server`
- `systemctl status rabbitmq-server`

## Tomcat/App setup

### download and install

- `vagrant ssh app01`
- `cat /etc/hosts`
- `dnf update -y`
- `dnf install epel-release -y`
- `dnf -y install java-17-openjdk java-17-openjdk-devel`
- `dnf install git wget -y`
- `cd /tmp/`
- `wget https://archive.apache.org/dist/tomcat/tomcat-10/v10.1.26/bin/apache-tomcat-10.1.26.tar.gz`
- `tar xzvf apache-tomcat-10.1.26.tar.gz`

### create tomcat user

- `useradd --home-dir /usr/local/tomcat --shell /sbin/nologin tomcat`
  - create user and home directory
  - give them no login
- `cp -r /tmp/apache-tomcat-10.1.26/* /usr/local/tomcat/`
  - copy the tomcat service to the new homedir
- `chown -R tomcat.tomcat /usr/local/tomcat`
  - change ownership of homedir and everything in to tomcat user and tomcat group

### create the service file for tomcat

- `vi /etc/systemd/system/tomcat.service`
  - fill this file with the following text
- ```text
  [Unit]
  Description=Tomcat
  After=network.target

  [Service]
  User=tomcat
  Group=tomcat
  WorkingDirectory=/usr/local/tomcat
  Environment=JAVA_HOME=/usr/lib/jvm/jre
  Environment=CATALINA_PID=/var/tomcat/%i/run/tomcat.pid
  Environment=CATALINA_HOME=/usr/local/tomcat
  Environment=CATALINE_BASE=/usr/local/tomcat
  ExecStart=/usr/local/tomcat/bin/catalina.sh run
  ExecStop=/usr/local/tomcat/bin/shutdown.sh
  RestartSec=10
  Restart=always

  [Install]
  WantedBy=multi-user.target
  ```

- `systemctl daemon-reload`
  - since we created a new service file we need to reload
- `systemctl start tomcat`
- `systemctl enable tomcat`
- `systemctl start firewalld`
- `systemctl enable firewalld`
- `firewall-cmd --get-active-zones`
- `firewall-cmd --zone=public --add-port=8080/tcp --permanent`
- `firewall-cmd --reload`

### code build and deploy (Maven)

- `cd /tmp/`
- `dnf install unzip -y`
- `wget https://archive.apache.org/dist/maven/maven-3/3.9.9/binaries/apache-maven-3.9.9-bin.zip`
- `unzip apache-maven-3.9.9-bin.zip`
- `cp -r apache-maven-3.9.9 /usr/local/maven3.9`
- `export MAVEN_OPTS="-Xmx512m"`
- `git clone -b local https://github.com/hkhcoder/vprofile-project.git`
- `cd vprofile-project`
- `vim src/main/resources/application.properties`
- Update file with backend server details
  - ```
    jdbc.url=jdbc:mysql://db01:3306/accounts?useUnicode=true&characterEncoding=UTF-8&zeroDateTimeBehavior=convertToNull
    jdbc.username=admin
    jdbc.password=admin123
    ```
  - this should already be done for this project but you can see the db url is db01:3306/accounts which are all part of the settings we added above
  - this is also using the username and password we made, make sure they are right
- _make sure you are in the vprofile-project dir_
- `/usr/local/maven3.9/bin/mvn install`
  - this will install Maven from the dir that we put it in earlier

### deploy artifact

- `ls target/`
  - notice vprofile-v2.war
  - this is an artifact, like .zip, for java.
  - we need to move this into the tomcat home dir
- `systemctl stop tomcat`
  - so we don't mess anything up
- `ls /usr/local/tomcat/webapps/`
  - this is already populated but it is where are putting this artifact
- `rm -rf /usr/local/tomcat/webapps/ROOT`
  - this root folder is the default for tomcat so we remove it and replace it
- `ls /usr/local/tomcat/webapps/`
  - make sure ROOT is gone
- `cp target/vprofile-v2.war /usr/local/tomcat/webapps/ROOT.war`
  - we are copying to this dir with a new name so that it becomes the root for the project
- `ls /usr/local/tomcat/webapps`
  - make sure that you can see the new root.war folder
- `systemctl start tomcat`
  - after starting you should see the ROOT folder repopulate
  - while you can do this by hand it is not needed because tomccat does it automatically
- `chown tomcat.tomcat /usr/local/tomcat/webapps -R`
- `systemctl restart tomcat`

## Nginx setup

### download and install

- `vagrant ssh web01`
- `sudo -i`
- `cat /etc/hosts`
- `apt update`
  - this is not ubuntu, you need apt
- `apt upgrade`
- `apt install nginx -y`

### create config file

- `vi /etc/nginx/sites-available/vproapp`
- put in this code snippet for the file

```
upstream vproapp {
  server app01:8080;
}
server {
  listen 80;
  location / {
    proxy_pass http://vproapp;
  }
}
```

- server
  - is listening on port 80
  - location is / or home dir
  - proxy_pass is telling it to use the upstream when you visit that site
  - upstream is where we set the forwarded server name and port
- `rm -rf /etc/nginx/sites-enabled/default`
  - remove default
- `ln -s /etc/nginx/sites-available/vproapp /etc/nginx/sites-enabled/vproapp`
  - this is just creating a link, this allows us to have several sites saved in the available folder but only the enabled folder is what is actively running
- `systemctl restart nginx`

## Validate (how did that work)

### Nginx and Tomcat

- back in bash
- `cat vagrant file`
  - find the web01 ip address
  - should be 192.168.56.11
- copy paste that into the url of a browser
  - you should see the login page load up after a bit

#### errors

- if ip is found but the page it not loading (maybe a white screen or a tomcat default page) then it is likely an nginx error that isn't seeing the html
- if you get a 404 page not found default error from the browser it is likely an nginx hosting error

### DB

- log in with the credentials admin_vp admin_vp
  - that was imported with the db when we unpacked that zip
- if you can log in then the db is hooked up correctly

#### errors

- if you can't log in or if you did login but there is no content you either didnt connect the db correctly or you didn't populate the db correctly

### RabbitMQ

- there is a RabbitMQ button towards the top of the page. click it and see if it returns a page with information about connections

### Memcache

- click the all users button and see if you get a gui for all the users in the database. this shows that is was cached correctly to allow for faster loading times
- you should also click on one of the blue ids and it will return a page that tells you the data is from the db and it is cached
- now hit back and press the same id again and it will load faster and say that the data is from cache

# Automated Project

## Code

- There is an automation folder already created in the source code
- if you look at the vagrant file then you can see that the provisioning sections all point to a .sh file, this keeps the vagrant file from being too large
- these .sh files are basically what we already did, just copied into a shell file
  - shell is not in sudo by default make sure to add the sudo before lines that need it like installing
  - difference for mysql, you can run executions on mysql but you need to login with user and pass everytime to do it
  - in tomcat, we create the file using cat command since you can't use vi or vim. start with <<EOT>> and end with EOT

## Execution

- make sure you halt all of your manual work
  - you can destroy them if you want
- navigate to the automation dir and vagrant up.
- now you can watch the magic on virtual box if you want or just watch in bash but either way nothing to do but wait.
- when its up you can check the vagrant file for the correct ip
  - should be 192.168.33.11
- log in and test just like last time
- done!
