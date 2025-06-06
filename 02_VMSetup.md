# Virtual Machine Setup

## Concept - what is virtualization

- you need to have 1 server per service or app
- best practice you should have 2 for redundencies
- if you a huge service then 3 or even more (aws has 12)
- 4 services = 8 servers which is a lot of money and set up
- Instead we can user VMs to run more OS on 1 machine and still keep isolation
- 1 hardware - the server rack
  - 1 hypervisor - a program that monitors all VMs like AWS
    - several VMs
      - 1 operating system per VM
        - 1 application per OS
- host OS - OS of the hyper visor or computer running VMS
- guest OS - OS of the VMs
- VM - virtual machins
- Snapshot - a small file that holds informtion that we can easily back up and upload into the VMs to make our lives easier
- HyperVisor - enables VMs
  - bare metal
    - run as an OS. this replaces windows or iOs
    - examples Xen HyperVisor, VMware Esxi
  - hosted - runs on a software - this is for learning and testing - oracle virtualbox, Vmware server
- [Visuals - click on Virtualization](https://www.visualpath.in/devopstutorials/devops)

## Creating the OS on the VM

- Manual
  - this requires a install wizard and takes a lot of time
- Automated
  - create a text file that you run automatically and installs on its own

### Manual - doing it by hand first to learn

- what you need
  - Oracle VM Virtualbox - hypervisor
  - ISO file - centOS or Ubuntu
  - Login tool -Git Bash & Putty
  - Enable virtualization in BIOs

### Automated

- what you need
  - Virtualbox - hypervisor
  - Vagrant - creates VMs from text file
  - Vagrant up - CLI tools

### Requirements

_* IMPORTANT ASUS BIOS SOMETIMES CALL IT SVM FOR NO REASON *_

- Enable VTX in BIOS
  - VTx
  - Secure virtural machine
  - Virtualization
- Turn off features in Windows (just search windows features in task bar)
  - Microsofr Hyperv
  - Windows Hypervisor platform
  - Windows Subsystem for linux
  - Virutal Machine Platform
- Reboot PC

## Manually Creating the VM

- Open up Oracle VM Virtualbox Manager
- click new - this is for red hat
  - name it whatever
  - change the folder to whatever
  - type - linux
  - version red hat 64bit
- next
  - base memory
    - 1024 MB is good for a small machine with low ram
    - 2048 MB is the preffered option if you have the ram to spare
  - processors - keep at 1 (unless you want to run crazy shit and slow your pc down a lot)
- next
  - you can change this how you want 20GB is enough for almost anything you want to do
  - do not check pre-allocate full size or you will lose 20 GB of you space until you delete it
- next
  - you can check stuff here make sure its right
- finish
- click new - this is for ubuntu
- differences from above
  - make sure it gets 2 CPUs
  - it should have 25GB also unallocated

### installing the OS

- search 'centos stream 9 iso download'
- click the first link [here it is](https://mirror.stream.centos.org/9-stream/BaseOS/x86_64/iso/)
- look for boot.iso (should be around 1 gig)
- click on that and it should download
- back on Oracle VM Virtualbox Manager
  - click on centos
    - click the settings gear on the top
    - go to storage tab
      - click on controller IDE that says empty
      - click the disk dropdown
      - click choose a disk file
      - click the iso that you downloaded
      - click the check box for live CD/DVD
    - in settings there is network tab
    - there should be 4 adapters
      - 1 should already be enabled
      - turn on 2 and attach it to bridge adapter
        - Name below should be your wireless or ethernet port
        - these adapters will either be called wifi something
        - or realtek PCIe something for ethernet
    - press ok, close that up
    - run start with the arrow on top
    - it should open up a small window
    - capture the mouse in it
      - right control will release the mouse
    - run install with the commands
    - finish set up
      - english - next
      - installation destination
        - click the partion then done on the top
        - you may need to do it again - just make sure you see 'Automatic partitioning selected'
      - network and host name
        - you should see 2 one is local in the VM, not good for anything
        - the other should be 192.168.1 or something similar
          - change the host name to something you know, like centosvm
      - root password - make it
        - hint for me - it's Cent OS
        - you can check the SSH is you want but its not necessary
      - complete installation - this will take a while
    - dont reboot system. shut down with virtual box
    - right click it in virtualbox and click stop -> ACPI shut down
    - when its done, go back to setting, storage, and remove the iso boot drive from the tray
    - then you can start the VM again and finish final set up, skip everything, add your username and password and your good to go!

## Automatically creating the VM

- Vagrant is a VM automation tool that we are using
  - This is not a hypervisor, is a manager
- Vagrant Benefits
  - no OS Installation
    - they use VM Images/Box
    - Vagrant cloud stores the OS and we make copies
  - VagrantFile
    - manage all VMs with 1 file if we need updates
    - provisioning CLI for all VMs at once
  - simple commands (CLI) - check commands file
    ![Vagrant Diagram](/img/vagrant.png)

### Getting started

- open gitbash
  - pwd - shows present working directory
- make a new directory in whatever drive you want
  - mkdir /w/vagrant-vms
- cd into the new drive
  - cd /w/vagrant-vms/
- make 2 more directories
  - mkdir centos
  - mkdir ubuntu
- you can check if it was made right with ls
- go to [vagrant cloud](https://portal.cloud.hashicorp.com/vagrant/discover) to find boxes
  - look up centos 9
  - you should see a bunch of pre-made boxes that you can use in the future if you want
  - we used [eurolinux-vagrant/centos-stream-9](https://portal.cloud.hashicorp.com/vagrant/discover/eurolinux-vagrant/centos-stream-9)
  - if you look at the link you can see that is supports virtual box, make sure what you want is supported
  - you should see the "How to use this box with Vagrant" section on the page, looks kind of like this
  ```js
    Vagrant.configure("2") do |config|
      config.vm.box = "eurolinux-vagrant/centos-stream-9"
      config.vm.box_version = "9.0.48"
    end
  ```
  - copy the name exactly e.g. "eurolinux-vagrant/centos-stream-9"
- go back to the same folder .../vagrant-vms/centos
  - type vagrant init {box name}
    - e.g `$ vagrant init eurolinux-vagrant/centos-stream-9`
  - make sure the vagrant file was created with ls
  - you can look at the file with cat VagrantFile
    - you can open this file and edit the name to make a new box
- make sure you are still in the right dir and type `vagrant up` to start the vm

  - POTENTIAL ERROR
    - `bsdtar.EXE: Error opening archive: Unrecognized archive format`
    - fix - updating vagrant
  - POTENTIAL ERROR
    - `schannel: next InitializeSecurityContext - Vbox hardening`
    - fix - turning off anti virus
  - POTENTIAL ERROR

    - ```md
      There was an error while executing `VBoxManage`, a CLI used by Vagrantfor controlling VirtualBox.

      The command and stderr is shown below.Command: ["startvm", "6cf63051-c7c5-41e8-86d2-08d900c27c6e", "--type", "headless"]Stderr: VBoxManage.exe: error: The virtual machine 'centos_default_1741221655223_43917' has terminated unexpectedly during startup with exit code 1 (0x1).

      More details may be available in 'C:\Users\kypec\VirtualBox VMs\centos_default_1741221655223_43917\Logs\VBoxHardening.log'VBoxManage.exe: error: Details: code E_FAIL (0x80004005), component MachineWrap, interface IMachine
      ```

    - fix upgraded vagrant and virtualbox using choco and the issue was solved

- once you finish vagrant up (this takes a while) you can run
  - vagrant box list - see its installed
  - vagrant status - see its running
- vagrant ssh to log into the vm
  - you should see the new user name of the console `vagrant@localhost`
- you can play around in the vm here and do what you want
- you can also see the machine live if you open up virtualBox
- when you are done
  - `exit` to logout
  - vagrant halt to turn off the vm
  - vagrant status to make sure its off
- create ubuntu now, move to the other folder, and repeat
  - we are going to use [ubuntu jammy](https://portal.cloud.hashicorp.com/vagrant/discover/ubuntu/jammy64) for the ubuntu one
