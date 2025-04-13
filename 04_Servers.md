# Vagrant and Linux Servers

## Vagrant IP, Ram & CPU

- go to ubuntu dir
- ls
- ls -a
  - you will see a .vagrant file that holds the .env info about this server
- vagrant destroy
- y
- vagrant global-status
  - we are going to to this section with a fresh install
  - make sure you don't see the ubuntu server on the list
- ls ~/.vagrant.d/
  - this is all the hidden stuff

### editing the vagrant file for more options

- open the Vagrantfile in the ubuntu dir with notepad or w/e
- Vagrant.configure("2") do |config|
  - this is the file that runs and starts the ubuntu server
- end
  - stops the code. (this is Ruby)
- uncomment line 52 - config.vm.provider "virtualbox" do |vb|
- uncomment line 58 - the corresponding end
- uncomment line 57 - upgrade the vb.memory = "1600"
  - you can make this anything you want and is how you increase the memory allocation
- under that line add a new line vb.cpus = "2"
  - this will let you customize the number of cpus on the vm
- uncomment line 40 - config.vm.network "public_network"
  - this allows us to create a bridge network or a physical machine on the local network
  - this will use a random ip address from your machine and will not get a public ip address for the internet
- uncomment line 35 - config.vm.network "private_network", ip: "192.168.33.10"
  - this will be a static IP address that will not change or be random
  - we are going to change this to "192.168.56.14"
    - 56 is the norm for virtual box
      _important_
    - do not start with 0 or 1 on the ip, those are used by other processes and can cause serious issues with networking, I used 14
- save and quit

### back to bash

- clear
- cat Vagrantfile
  - make sure its updated correctly
- vagrant up
  - this is because we destroyed it. other wise vagrant reload would be enough

#### lets check out the output from vagrant

- `default: Adapter 1: nat`
  - this is the default router or 10.0 used only by vagrant for ssh
- `default: Adapter 2: hostonly`
  - this is the private network with the static ip
- `default: Adapter 3: bridged`
  - bridged public network

### back to bash

- vagrant ssh
- clear
- free -m
  - total 1521 - this is around 1.5GB of memory for the 1600 we assigned it
- cat /proc/cpuinfo
  - `cpu cores : 2'
  - towards the top, this shows that we did infact give it 2 cores
  - you can also check all of this on the Oracle VirtualBox Manager
- exit
- vagrant halt

## Vagrant Sync Directories

- vagrant up
  - `default: W:/vagrant-vms/ubuntu => /vagrant`
  - this is the host machine path => VM path
- ls
  - only Vagrantfile
- touch test1.txt
- ls
  - now 2 files
- ls -a
  - you can see 2 files and a dir
- vagrant ssh
- clear
- cd /vagrant
- ls
  - you will see your test file in there
  - this is a sync directory. this is synced with the host machine and vice versa
- touch file{1..20}.txt
  - look at the host machine path and you will see it update in real time as you add these files
- rm -rf file\*
  - removes all the files we just made
- ls

### more updates to the Vagrantfile

- uncomment line 46 - config.vm.synced_folder "../data", "/vagrant_data"
  - first argument is the host path and the second is the vm
- `config.vm.synced_folder "../data", "/opt/scripts"`
- create a folder in your drive, W:/scripts/shellscripts
  - you need to make sure to create the folder, the host machine needs to be created the VM will create it automatically
- `change to - config.vm.synced_folder "W:\\scripts\\shellscripts", "/opt/scripts"`
  - you need to use \\ instead of / for windows machines
- you are able to make as many of these as you want so you can sync several dirs
- the host machine can store common scripts for all of them to use
- the host machine can act as a backup for important files
- lastly you can create a folder for logs to see errors

### bash

- exit
- vagrant reload
  - you should be able to see the new synced folders in the load
  - `default: W:/scripts/shellscripts => /opt/scripts`

## Provisioning

- shell is a provisioner, there are others like chef, and puppet
- this is code that runs at server creation.
- this is not interactive and can not complete in a question
  - using -y at the end of commands is one way around this

### example running on a new server

- this is going to include examples, please destroy centos vm
- go to the vagrant file for centos
- turn on the bridged public network
- turn on the private network, make sure its a different ip
  - I used 192.168.56.16
- scroll to the bottom and look for the provisioning section
- uncomment the last 4 lines config.vm.provision down to SHELL
- change the middle lines between -SHELL and SHELL
  ```
  yum install httpd wget unzip git -y
  mkdir /opt/devopsdir
  free -m
  uptime
  ```
- save
- back to bash
- navigate to centos
- tail Vagrantfile
  - make sure you see the changes
- vagrant up
  - you can see all of the commands run
- vagrant reload
  - you won't see the provisioning run
  - you will see a line that says 'Machine already provisioned'

### example running on existing server

- uncomment the same line in the ubuntu Vagrantfile
  - leave it as is, apt can run on ubuntu
- tail Vagrantfile
  - make sure that it has the changes
- vagrant reload --provision
  - this will reload and force the provision on an existing server
- since this will install and run apache the server should already be up and running
- take the ip address you put on the private server and put it in a browser address bar
  - http://192.168.56.14
- you will see the apache2 default page if it worked corretly!

## Website setup

- start by destroying all ubuntu and centos vms
- we are going to create a vm that will automatically boot and run a website
- this is what we came for folks
- get a website, you can make it or take a free one from tooplate.com

### getting started

- you can use any template but I chose mini finance
- make a new folder W:/vagrant-vms/finance
- run vagrant box list
- we are going to use centos
  - _eurolinux-vagrant/centos-stream-9_
- navigate to the finace folder and run vagrant init {box name}
- once it finishes you should have vagrant file
  - ls to look for it
- open vagrant file,
  - create a private network, 192.168.56.22 for me
  - create public network
  - uncomment vb.memory = '1024'
  - save and quit
- you can also use vim to edit the file or check your work
- vagrant up
- vagrant ssh
- sudo -i
- create a hostname so we knows whats up
  - vi /etc/hostname
  - finance
  - :wq
- cat /etc/hostname
- hostname finance
- exit
- exit
- vagrant ssh
  - you should now see vagrant@finance
- sudo -i
  - to host a site we use httpd on centos
  - to host a site we use apache2 on ubuntu
- yum install httpd wget vim unzip zip -y
  - httpd to host
  - wget to download the template
  - unzip to unzip the template after download
  - zip not really required but you should have it if you have unzip
  - vim is just a better vi
- systemctl start httpd
- systemctl enable httpd
- ip addr show
  - you can check inet 192.168.56.22
- go to http://192.168.56.22 and see that it is live
  - the test page tells you to add content at /var/www/html
- clear
- cd /var/www/html
- ls
  - it should be empty
- vim index.html
- add `<div> hello world </div>`
- systemctl restart httpd
- navigate back to http://192.168.56.22
  - there is your work

### hosting finance

- go to tooplate and find the download link for the finance page
- the actual download link will be a .zip route that you can find on the network tap of the inspect dev tools
  - https://www.tooplate.com/zip-templates/2135_mini_finance.zip
- cd /tmp/
- wget https://www.tooplate.com/zip-templates/2135_mini_finance.zip
- ls
  - if you did it right you will see a file with .zip at the end, if you did it wrong then you will just see a file.
- unzip 2135_mini_finance
- cd 2135_mini_finance
- clear
- ls
  - you should see everything including the index.html
- cp -r \* /var/www/html/
  - copy recusively (everything) all files and folders into the /var/www/html folder
- y to overwrite
- refresh the webpage and you should see the
- you can delete this if you want to

### debugging

- systemctl restart httpd
- ls /var/www/html
- systemctl status firewalld
  - this could prevent outside connection, it happens on some machines and OS's but not all
  - if it is enabled and your site isn't working you can use
- systemctl stop firewalld
- systemctl disable firewalld
  - this is not the proper way to deal with this error but its good enough for now, we are just learning servers

## Wordpress setup

- google wordpress on ubuntu
  - Install and configure WordPress from ubuntu site
- read the clear step by step instructions
- I have no reason to look more into this. if you want to go for it

## Automate Website setup

- we are going to setting this all up with provisioning
- I wrote the step I took above, you can basically copy those into the provisioning section and have it run nicely

### here we go

- open the vagrant-vms folder on vscode, or you cn practice more vim if you want
- we are going to make a copy of finance dir and name it financeIAC (that stands for infrastucture as code)
  - It is important naming on the file so people can easily see that it is an automated file
- delete the .vagrant file so we can start with a fresh vm
- open up the Vagrantfile
- change private network to 192.168.56.28
- go to the bottom and set up all the instructions in provisioning
  - yum install httpd wget unzip zip vim -y
  - systemctl enable httpd
  - systemctl start httpd
  - mkdir -p /tmp/finance
  - -p means if the folder already exists don't error
  - cd /tmp/finance
  - wget https://www.tooplate.com/zip-templates/2135_mini_finance.zip
  - unzip -o 2135_mini_finance.zip
  - -o means overwrite so if it exists it wont error
  - cp -r 2135_mini_finance/\* /var/www/html
  - systemctl restart httpd
  - cd /tmp
  - rm -rf /tmp/finance
  - delete the folder to save room and prevent caching errors
- save
- navigate to folder in bash
- vagrant up
- you can watch it work
- when its done you can go to http://192.168.56.28
- tada

## you can automate the wordpress too but I dont wanna

## Multi VM Vagrantfile

- normally there is 1 vm per Vagrantfile
- you can have multiple VMs on the same file
- this is really important if you want to make several servers to manage different operations in 1 task
  - a server for the data
  - a server for the frontend
  - a server for the backend
  - a server for the images
  - and so on
- you can google vagrant docs and look up all the file settings
  - this also includes all CLIs to help
- we are looking for multi machine
- you can find a sample of what the file should look like in that doc

```ruby
  Vagrant.configure("2") do |config|
    config.vm.provision "shell", inline: "echo Hello"

    config.vm.define "web" do |web|
      web.vm.box = "apache"
    end

    config.vm.define "db" do |db|
      db.vm.box = "mysql"
    end
  end
```

- you can add all of the settings that we have been doing in the past files in the multifile
- you can use chatgpt for this work too but make sure you aren't relying on it too much
- chatgpt
  - Multivm Vagrantfile with web01 ubuntu20, web02 with ubuntu20, and db01 with centos7. Private IP for all the VMs. Provisioning for db01. set hostname also.
- my sample is in the [samples/04/multiVM](samples/04/multiVM)
  - I did need to update the yum install line to incluide zip, unzip and wget
  - There was an error on the install, something went wrong with internet access, all I did was vagrant reload and it worked to problem

### example

- create a new folder in Vagrant-vms
- make a new file called Vagrantfile
  - no extention capital V
- paste the sample there
- open bash
- go to the Multivm dir
- vagrant up
  - this will take a while because its 3
  - make sure that you don't have other stuff running, this will slow down you pc a lot
- you can enter these with vagrant ssh web01 etc.
- you can also vagrant up web01 or vagrant halt db01 etc
- vagrant halt to turn these all off when your done

## Systemctl & Tomcat 10

- there are some services that do not have a systemctl by default
- tomcat is similar to httpd but used for very different things
- it is an open source java servlet container
- this means that you can host java based web applications
- this requires centOS to run

### downloading and running

- vagrant up the centos vm
- vagrant ssh
- sudo -i
- clear
- dnf install httpd -y
  - this isn't required if your provisioning still includes httpd, double check
- systemctl status httpd
  - should be installed but inactive
- ls /usr/lib/systemd/system/
  - on this list you will find httpd.service
- ls /usr/lib/systemd/system/ | grep "httpd"
  - will help you find it easier but its good to see how many services/sockets there are on the machine
- cat /usr/lib/systemd/system/httpd.service
  - in this file we have 3 directives
    - Unit
    - Service
    - Install
  - look in Service and find ExecStart = /usr/sbin/httpd $OPTIONS -DFOREGROUND
    - this command is the one that runs when we start the service
- ls /etc/httpd/
  - this is the config file
- ls /var/logs/httpd
  - this is where the log files go
- google download [tomcat 10](https://tomcat.apache.org/download-10.cgi)
  - click first link
  - find binary distribution
  - core
  - tar.gz (this is for linux/centos)
  - right click, copy link address
- wget [tomcat address](https://dlcdn.apache.org/tomcat/tomcat-10/v10.1.40/bin/apache-tomcat-10.1.40.tar.gz)
  - extract it
- tar xzvf apache-tomcat-10...
- ls apache-tomcat-10.1.40
  - you can see all the binaries, logs, config etc.
  - in order to run this you need java
- dnf install java-17-openjdk -y
  - this is a HUGE install. still shouldn't take more than a minute
  - once complete we can test
- java -version
  - you should see 17.0.14 or whatever its at now
- ls
  - make sure you are still in the apache-tomcat dir
- ls apache-tomcat-10.1.28/bin
  - you will see startup.sh
  - this is the shell script that will start the service
- cd apache-tomcat-10.1.28
- bin/startup.sh
  - you should see some text and then Tomcat started.
  - lets check the processes and make sure its running
- ps -ef | grep tomcat
- ip addr show
  - take any of the public ips (the ones starting with 192.168) and paste them into your browser followed by port 8080
  - `http://192.168.56.16:8080`
  - kill the process
- ps -ef | grep tomcat
  - find the process number, its towards the beginning
- kill 9605
  - there will be one left but its not required to kill

### running this service automatically at boot

- first things first, every service should be run by their own user that is NOT a root user so we need to make a new user. AND since this is centos there will not be an automatic home directory for that user
- useradd --home-dir /opt/tomcat --shell /sbin/nologin tomcat
  - --home-dir defines a default home directory that the user will be in when running
  - --shell nologin means that this user will not be able to ssh into or log into. this user is purely a bot that will run a service
- cp -r apache-tomcat-10.1.28/\* /opt/tomcat
  - move all the tomcat stuff into that dir
- chown -R tomcat.tomcat /opt/tomcat
  - since we downloaded the folder in root we need to assign the newuser as the owner of the folder and not root.
  - -R will work recursively to make EVERYTHING in the /opt/tomcat dir owned by the user tomcat and the group tomcat
- ls -l /opt/tomcat
  - make sure that all the stuff is now owned by tomcat user and group
  - now lets create the service file in system
- vim /etc/systemd/system/tomcat.service
  - the last part is the name of service that is running. it can be anything

#### tomcat.service notes

- the rest of this will be notes and the finished file will be in [samples/04/tomcat.service](samples/04/tomcat.service)
  - we need to write this like the others and remember there are 3 directives
  - also make sure to capitalize all the things
  - These are rarely written from scratch like this but its good to practice
    - normally they will be on the docs or internet or you can pull from an existing one or even chatgpt
- [Unit]
  - this holds information about the service, descript and dependencies
  - Description= what will show you look up processes and sevices
  - After= defines the dependencies and will act like a stop gap, waiting for something to happen first before running
- [Service]
  - Type= we are using forking which just means that this service can make child processes
  - User= defines the user that will be running this service we made tomcat for that
  - Group = defines the group this will also be tomcat
  - WorkingDirectory= shows where its working out of, we made this the home-dir of the tomcat user
  - Environment= there can be several of these and they are usually a requirement of the service.
    - for example tomcat requires java
  - ExecStart= directory to the shellscript that will start the service
  - ExecStop= directory to the shellscript that will stop the service
- [Install]
  - WantedBy= this is server admin stuff, we can learn more about it later but surface level there are 3 start up options, safemode, gui, and complete os-startup
    - we are using multi-user.target and that is complete os-startup minus the gui

#### end of tomcat.service notes

- make sure to save a quit, I have the sample in the folder
- systemctl daemon-reload
  - when you make any changes to the service you should always run this to refresh the commands
- ps -ef | grep tomcat
  - make sure no tomcat processes are running
- clear
- systemctl start tomcat
- systemctl status tomcat
  - you should see an active service running call Tomcat
- systemctl enable tomcat
  - now that we created a file to run tomcat as a service we are able to enable it. meaning it will now run at boot
- more importantly in the future when we are running managers like ansible in the future the systemctl is required to manage services.
  - even if you did the provisioning required to make it work its still not the right way to do it
