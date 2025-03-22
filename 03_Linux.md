# Linux tutorial

## Some important directories

- home directories
  - /root
  - /home/{username}
- user executables
  - /bin
  - /usr/bin
  - /usr/local/bin
- System executables
  - /sbin
  - /usr/sbin
  - /usr/local/sbin
- other mountpoints
  - /media
  - /mnt
- Configuration
  - /etc
- Temporary Files
  - /tmp
- Kernels and bootloader
  - /boot
- Server Data
  - /var
  - /srv
- System Information
  - /proc
  - /sys
- Shared Libraries
  - /lib
  - /usr/lib
  - /usr/local/lib

## commands and file systems

- start up a vagrant vm (up, ssh)
- type pwd to see the path to their home directory
  - it should be the same as the user in the prompt (vagrant@localhost)
- cat /etc/os-release
  - shows all of the information about this version of linux
- notice that you have a '$' at the start of your text, that means that you are on a normal user
- if you type in sudo -i you will switch to the root user and you will see a '#' meaning that you are the root user
  - type in pwd and see that you are now in /root
- type in cd /
  - this will bring you to the root directory which is different than the root user's home directory
  - type ls and it will show you all the basic directories in linux

### /bin

- if you navigate to /bin and type ls you can see all of the user commands like the ones we have been using, ls, whoami, pwd, ...

### /sbin

- if you navigate to /sbin and type ls you can see all of the system commands that can only be used by a root user like mkfs.ext4, this is used for creating a partition

### /etc

- if you navigate to /etc you can see a list of all of the system configuration files
  - you can then type in cat {file name} to see what each file's configs are line cat /etc/hostname. at the start this will just be localhost@localdomain

### /tmp

- /tmp holds all of the temporary files that your programs might need to run commands.
  - /this is where we are going to be storing information for access later if we need it

### /boot

- /boot holds your kernels
- this is also where you hold the grub and grub2 where you can customise the booting parameters. mostly used for system
  administration

### /proc

- these are process files, they are dynamic and change constantly based on the system information
- a good example of this is the uptime file is stored here
  - type 'uptime' and you will see information about this session
  - but if you type in 'cat /proc/uptime' you will still the information but it will not be user readable

## most common commands

### put them all on the Linux Commands Page

## VIM Editor

### install vim

- vim is not installed by default but you can install it with console
- sudo yum install vim -y
- vim has 3 modes
  - command mode (default)
  - insert mode (edit mode)
  - extended command mode
- you can move from command mode to insert mode with 'i'
- you can move from insert to command with esc
- you can move from command to extended command with ':'

### more commands are found in the commands folder

### practice - this is on centos

- sudo -i
- ls (find anaconda)
- cat anaconda-ks.cfg
- vim anaconda-ks.cfg
- :se nu - set line numbers
- G - skip to end
- gg - to go top
- down arrow - move to line 12
- yy - copy line 12
- G
- p - paste
- P - paste above
- gg - go back to line 12
- 4yy - copy 4 lines
- gg
- dd - delete line 1
- u - undo
- 5dd delete 5 lines
- p
- 999dd - delete whole file
- u
- esc
- :q! dont save

## File Types

- ls -l
  - shows every file that you can have in the directory with extra info
    - drwxr-xr-x || -rw-------
  - look at the first letter if it has a d its a directory and a - means a file

### list of types

- d - directory
- - - file
- l - link to another file
- c - special file - input output
- s - socket - for inter process networking
- p - pipe - allows processes to communicate without network sockets

### practice

- mkdir /opt/dev/ops/devops/test
  -this will error because you don't have all those dirs
- mkdir -p /opt/dev/ops/devops/test
  - this will make all the dirs that you need to complete this
- vim /opt/dev/ops/devops/test/commands.txt
- i
- add commands to the file like whoami, ls, mkdir, uptime, touch, cd, pwd
- esc
- :w
- :q
  - this new file is very far into the dirs so we can create a link
- ln -s /opt/dev/ops/devops/test/commands.txt cmd
- ls -l
  - you shouls see the new link file on the list
- cat cmds
- mv /opt/dev/ops/devops/test/commands.txt /tmp
  - we are moving the file to tmp to show an error
- ls -l
  - error, it's linking to a nothing, its now red to show
- mv /tmp/commands.txt /opt/dev/ops/devops/test
- ls -l
  - its live again
- unlink cmds

### more practice

- updating host name
- vim /etc/hostname
- i
- Centos.DevOps
- hostname centos.devOps
- exit
- exit
- vagrant ssh
  - when it starts you should see the host name is now centos
- hostname
  - this will output the hostname
  - the displayed one is the {centos}
  - the saved one is {Centos} so you can see which is from the file and which is from the command
- ls -ltr /etc
  - you will see that the last file to be updated was the hostname one

## filters

### grep

- sudo -i
- ls
  - we are going to use the anaconda file
- grep firewall anaconda-ks.cfg
  - you should see the line that says firewall disabled
- grep Firewall anaconda-ks.cfg
  - case sensitive
- grep -i firewall anaconda-ks.cfg
  - -i ignores cases
- grep -i firewall \*
  - shows all instances in all the files in the directories
- cp anaconda-ks.cfg devopsdir/mybootingfile.cfg
- grep -iR firewall \*
  -searches all files in all directories for the word
- grep -R SELINUX /etc/\*
- grep -iv firewall anaconda-ks.cfg

### less

- less {file}
- less is a reader like vim but not an editor
- you can type /{search} to find a sting in the less file

### more

- like less but worse

### head/tail

- head is the first 10 lines of a file
- tail is the last 10 lines of a file
- you can also use tail -f to watch a file
- example
  - first terminal
    - tail -f /var/log/messages
  - second terminal
    - open second git bash screen
    - ssh into centos
    - sudo -i
  - look at the messages update live on the log file in the first termial

### cut

- there are files that are sperated by a delimitator
- cut can be used to split the colomns to see easier
- example
  - cut -d: -f1 /etc/passwd
    - this will cut by the delimiter : and return the first colomn of passwd

### awk

- better cut
- awk -F':' '{print $1}' - same as cut above

### sed

- search and replace
- sed 's/{search}/{replace}[/g]' {file}
- /g is global

## output redirection

### > or >>

- \> replaces a file
- \>> appends a file
- practice
  - echo "#####################################" > /tmp/sysinfo.txt
  - echo date > /tmp/sysinfo.txt
  - echo "#####################################" >> /tmp/sysinfo.txt
  - echo uptime >> /tmp/sysinfo.txt
  - echo "#####################################" >> /tmp/sysinfo.txt
  - echo free -m >> /tmp/sysinfo.txt
  - echo "#####################################" >> /tmp/sysinfo.txt
  - echo df -h >> /tmp/sysinfo.txt
  - echo "#####################################" >> /tmp/sysinfo.txt
  - cat /tmp/sysinfo.txt
- 2> only shows errors
- 1> default shows output
- &> shows either
- you can send them to the right folder with
  - freeee -m 2>> /tmp//error.log

### /dev/null

- this is a black hole for text
- if you install something and you don't want to see the terminal output you can use
  - yum install vim -y > /dev/null
- you can also use it to clear files
  - cat /dev/null > /tmp/sysinfo.txt

## output piping

### piping command |

- wc -l /etc/passwd
  - 25
- this will pipe the output into a different command
- ls | wc -l
  - 186, this is the amount of files in the dir
- ls | grep host
  - shows all files that start with the word host
- tail -20 /var/log/messages | grep -i vagrant
  - shows anytime the word vagrant shows up in the last 20 lines
- free -m | grep Mem
  - shows only the line for Mem
- ls -l | tail
  - last 10 files
- ls -l | head
  - first 10 files

### find

- find /etc -name host\*
  - finds all files in /etc that start with the word host

## users and groups

- every file on the system is owned by a user and associated with a group
- every process has an owner and group affiliation, and can only access the resources its owner or group can access
- every user has a UUID
- every name and UID is stored in /etc/passwd
- passwords are stored in /etc/shadow in an encrypted form
- users are assigned a home directory and a program that is run when they login (usually a shell)
- users cannot read, write, or execute each other files without permission

### types of users

- ROOT
  - uid - 0
  - group id - 0
  - home dir - /root
  - shell - /bin/bash
- Regular
  - uid - 1000 to 60000
  - group id - 1000 to 60000
  - home dir - /home/username
  - shell - /bin/bash
- Service
  - uid - 1 to 999
  - group id - 1 to 999
  - home dir - /var/ftp
  - shell - /sbin/nologin

### user brake down

- head -1 /etc/passwd
  - root:x:0:0:root:/root:/bin/bash
  - name root
  - password x - hidden
  - uid 0
  - group id 0
  - comment root
  - home /root
  - shell /bin/bash
- grep vagrant /etc/passwd
  - you can see the differences here
- cat /etc/passwd
  - look at some more and see how they work
  - you can see that a lot of them have a shell of /bin/nologin

### group file

- cat /etc/group
  - show info on all the groups in the system
  - name of group, password, group number, and then any users in the group

### users

- you can use id {username} to find out information about a user
- useradd {username}
  -adds a new user to the system
- useradd - kyle
- useradd - randy
- tail -4 /etc/passwd
  shows the new users and their information all added automatically
- id john

### groups

- group add devops
  - creates a new group
- usermod -aG devops kyle
- id kyle
  - kyle will now have 2 groups associated
- grep devops /etc/group
  - you can see that the group now has kyle as a user

---

- you can also directly add them to the root file
- vim /etc/group
- /devops
  - finds the group
- add john to the list
  - even though john is not a user yet you can add him
- useradd john
- id john
  - you can see that john has already been added to this

### passwords

- you can add a password to any account
- you can reset it in the same way
- passwd kyle
- pass
  - it will warn you about bad passwords.
  - this is optional but in a real system make them good
- pass
- tail -4 /etc/passwd
  - it still shows x as the pass because its encrypted

### switch users

- switch with su
- su kyle
- pass

### tracking users

- last
  - shows you who logged in last and who is still logged in
- lsof is a library that you can get from yum
- yum install lsof -y
- lsof -u vagrant
  - shows files and logins of that user
- lsof -u kyle
  - unless you made or opened files with this user there should be nothing shown
- lsof -u root

### removing users

- userdel randy
- id randy
- ls /home
  - even though randy was deleted the home dir is still there
- useradd randy
  - it breaks because the home dir is still there
- userdel -r john
- ls /home
  - now john's home dir is also gone
- rm -rf /home/randy
  - you can remove the left over home dirs like this
- groupdel devops
  - you can also delete a whole group

### file permission

- ls -l
- grabbing devops dir
- drwxr-xr-x. 1 root root 2232 dec 6 08:32 anaconda-ks.cfg
  - d file type
  - rwx -> user write and execute permissions
  - r-x -> group permissions
  - r-x -> other permissions
  - 1 means
  - owned by root user
  - associated to root group
- anaconda file
  - -rw-------
  - only the root user can read and write to this file and no one else
- if you look at a link it will show you the permissions for the link and not for the file that it points to

### adding permissions to groups and users

- groupadd devops
- useradd john
- useradd randy
- useradd aws
- useradd jenkins
- vim /etc/group
  - find devops group
- add aws,randy,jenkins,john
- id randy
  - make sure he is in group devops
- mkdir /opt/devopsdir
- ls -ld /opt/devopsdir
  - the owner is root and the group is root
- chown randy:devops /opt/devopsdir
- ls -ld /opt/devopsdir
  - the owner and group is now updated
- chmod o-x /opt/devopsdir
  - read as 'change mod, other minus x'
  - removes executable from the others
  - can't use executables, can't 'cd' into this dir
- ls -ld /opt/devopsdir
  - you can see that the other went from r-x to r--
- chmod o-r /opt/devopsdir
- ls -ld /opt/devopsdir
  - now other is ---
- chmod g+w /opt/devopsdir
- ls -ld /opt/devopsdir
- id kyle
  - make sure he is not in the group devops
- su kyle
- cd /opt/devopsdir
- ls /opt/devopsdir
  - both will have permission denied, cd is x, ls is r

### changing permissions

- chmod [-option...] mode[,mode] file|directory
  - mode includes
    - u,g,o
    - +,-,= grant, deny, set
    - r,w,x
  - options include
    - -R, recursive
    - -v, verbose
    - --reference, reference another file for its mode
  - examples
    - chmod ugo+r file
    - chmod o-wx dir
- chmod ### can change all at once
  - 4 is read
  - 2 is write
  - 1 is execute
  - 0 is none
  - if you want to do more than 1 just add
    - 6 is read and write
    - 7 is read write and execute
    - 3 is write and execute
  - first number is user then group then other
  - examples
    - chmod 770 dir
    - chmod -R 346 file

### sudo

- sudo is permission that will allow a user to execute commands like a root user
- any user can have sudo powers0

#### this also allows any user to use the sudo command to authorize themelves

#### _IT IS NOT RECOMMONDED TO UPDATE THIS FILE MANUALLY_

- ls -l /etc/sudoers
  - no one can edit this file, not even root has w permissions for security
- visudo
- :se nu
- /root
  - there are a few but we are looking for line 100
- yy - copy
- p - paste
- change the name to kyle ALL=(ALL) ALL
- :wq
- su kyle
- sudo -i

#### you can also remove password requirments

- visudo
- /kyle
- kyle ALL=(ALL) NOPASSWD: ALL

#### visudo file errors

- if you enter something wrong the terminal will tell you
- syntax error line 9
- what now?
- type e

#### sudo a group

#### _THIS IS THE RECOMMENDED WAY TO ADD SUDO_

- cd /etc/sudoers.d
- ls
  - should see vagrant
- cat vagrant
  - %vagrant ALL=(ALL) NOPASSWD: ALL
  - % means that it is a group and not a user
- cp vagrant devops
- vim devops
- i
- edit to %devops ALL=(ALL) NOPASSWD: ALL
- esc :wq
  - now you should be able to sudo with anyone in the devops group like randy
  - if you need to check who don't forget that you can do cat /etc/group

## package management

- centos and ubuntu have different ways to manage their packages
- centos is apian os
- ubuntu is debian os

### centos / manual rpm

- sudo -i
- cat /etc/os-release
  - you can see that it is centos
  - NAME="CentOS Stream"
  - VERSION="9"
- arch
  - x86_64
  - this command will tell you the architecture
- rpm -qa
  - this will show all packages installed on this computer
- dpkg -l
  - this will error because this is debian
- telnet
  - this will fail because you don't have the package installed
- _on your main pc_
- search telnet rpm on the google
- choose whichever, i used rpmfind.net
- it will give you a large list
- make sure to find the same os you have
  - CentOs Stream 9 for x86_64
  - the name, version and arch from the above
- right click the link and copy link address
- _back on vagrant bash_
- curl {link} -o {name of package}
  - curl https://rpmfind.net/linux/centos-stream/9-stream/AppStream/x86_64/os/Packages/telnet-0.17-85.el9.x86_64.rpm -o telnet-0.17-85.el9.x86_64.rpm
  - you can paste link with shift+ins
  - you will see a little ui with download information if you did it right
- ls
  - you should see the .rpm
- rpm -ivh telnet-0.17-85.el9.x86_64.rpm
  - -i is for install
  - -v is for verbose - printing info
  - -h is for human readable
  - requires sudo
- telnet
  - should pull up cli's
- quit
- rpm -qa | grep telnet
  - will show you the package, copy it
- rpm -e {telnet package}
- rpm -qa | grep telnet
  - it should be gone

#### the problem

- lets install httpd
- search it on rpmfind
- copy link
- wget {link}
  - wget is like curl but only for installing so you don't need the -o and path
- rpm -ivh httpd---.rpm
  - it will fail due to missing dependencies
  - to solve this you would need to install ALL of them manually

### a better way

- yum can do it for us, we did it earlier
- cd /etc/yum.repos.d
- cat centos.repo
  - you will see a bunch of repos in the file
  - you will also see the links used to download them
- yum search httpd
  - it will show you all of the libs with the matching name
  - check "Name Exactly Matched"
  - if it is what you were looking for
- yum install httpd
  - it will list the package and all dependencies
  - that would have taken forever to install all 11 deps
- dnf install httpd
  - this is an alternative and newer, better option
- dnf remove httpd
  - it will remove http and all unused deps
- dnf upgrade
  - will update the whole system and all deps

#### practice - install jenkins

- search installing jenkins
- click linux
- there are different os's
  - choose red hat for appian
- there will be LTS release
  - you can copy and paste all this
  - first gets jenkins repo and put in jenkins.repo dir
  - next imports the key
  - next it makes sure your OS is upto date
  - next it installs fontconfig and java-17
  - next is jenkins
  - last it restarts your os

## Services

### httpd

- httpd is a service host for linux
- dnf install httpd
- systemctl status httpd
  - you will see that is says inactive
- systemctl start httpd
- systemctl status httpd
  - you should now see it running
- reboot
- vagrant ssh
- sudo -i
- systemctl status httpd
  - you can see that it is inactive
- systemctl enable httpd
  - this will start httpd at boot
- reboot
- vagrant ssh
- systemctl status httpd
- systemctl is-active httpd
- systemctl is-enabled httpd
- ls /etc/systemd/system/multi-user.target.wants
  - this is a list of all the services available
- cat /etc/systemd/system/multi-user.target.wants/httpd.service
  - this is a description of httpd service
  - ExecStart=/usr/sbin/httpd $OPTIONS -DFOREGROUND
    - this is the executed binary to start the service

## processes

- process are things that are constantly running on your os
- top
  - this will show you all the dynamic processes that are running on your os
    _load average is important_
    - if the load average starts to go up then the cpu is full
    - the 3 numbers are current, last 5 min, and last 15 min
- q
- ps aux
  - this is like top but is just a snapshot
- ps -ef
  - just shows pids and ppid (the parent process)
- ps -ef | grep httpd
  - this will show all process with httpd, the last is the grep command we ran to get it
- ps -ef | grep httpd | grep -v 'grep'
  - looks at the pid for the httpd
  - you will see a bunch but all of them point to the same parent execpt 1, kill that one
- kill {pid}
- ps -ef | grep httpd | grep -v 'grep'
- sometimes kill wont work then you need to force kill it
- kill -9 {pid}
- ps -ef | grep httpd | grep -v 'grep' | awk '{print $2}
  - this gives a nice print out of every pid you will need to kill if there is no parent process
- ps -ef | grep httpd | grep -v 'grep' | awk '{print $2} | xargs kill -9
  - this will pass all the pids to the force kill command

### zombie processes

- a child process that remains running even after its parent process is reminated or completed without waiting for the child process execution is called an Orphan process
- Zombie process has completed its task but still, it shows an entry in a process table
- normally they won't consume resources but they may fill your ram and lead to a crash
- these can't be killed because there is no pid attached to them.
- you can find the number of zombies with ps -ef
- the best way to remove them is to restart the os

## archiving

### tar

- cd /var/log
- ls jenkins/
  - you should see jenkins.log
  - devops will often archive logs for exporting
- tar -czvf jenkins_03222025.tar.gz jenkin
  - tar is short for tarball
  - c is so create
  - z is to compress
  - v is for verbose
  - f is for file
  - jenkins... is the file name and time stamp
  - tar is file type for tarball
  - gz is creating with compression
  - jenkin - what you are tarballing
- ls you should see the .tar.gz file
- mv jenkins_03222025.tar.gz /tmp/
- cd /tmp/
- ls
  - make sure you can see the file
- tar -xzvf jenkins_03222025.tar.gz -C /opt/
  - this will extract it to /opt
    -ls /opt

### zip

- this is simpler but has less options
- this is not on the base os like tar
- yum install zip unzip -y
- zip -r httpd_03222025.zip httpd
- ls
  - you should see your .zip file
- mv httpd_03222025 /opt
- cd /opt
- ls
  - you wont see the httpd dir
- unzip httpd_03222025/zip
- ls
  - you should see the httpd dir

## Ubuntu commands

### useradd

- this work similar but it will not create a root dir for the user
- instead use adduser
- this will create all the things and propt for password and more

### visudo

- opens the sudo file in nano, not vim
- we can change it back to vim with
- export EDITOR=vim
- this only works for your current session, if you reboot you will need to run again

### yum

- instead of yum we have apt
- cd /etc/apt
- ls
- cat sources.list
  - will show you all packages that you install
- apt update
  - must be done manually, yum checks and runs every 24 hours
- ubuntu has SO MANY more packages
- instead of httpd it has apache2
- apt install apache2
- y
- systemctl status apache2
  - ubuntu will automatically start and enable any service that you install
- apt remove apache2
  - will remove package but not config files
- apt purge apache2
  - will remove everything that came from it cleanly
