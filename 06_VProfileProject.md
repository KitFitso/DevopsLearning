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
