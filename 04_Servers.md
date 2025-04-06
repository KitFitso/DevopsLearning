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
