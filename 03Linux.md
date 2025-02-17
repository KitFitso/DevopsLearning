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

### mkdir {dirname}

- creates a directory
- follow for practice - make sure you are not in root 'exit' if needed. should say vagrant@localhost
  - cd
  - ls
  - mkdir dev
  - mkdir ops backupdir
  - ls
- you should now see that we made 3 dirs, if you make a spaced list they will be created seperately

### touch {filename}

- touch creates empty files
  - touch testfile1.txt
  - ls
- you should see your new file on the list
- you can also use this to create an array of files using {} and ..(please note only 2 dots)
  - touch devfile{1..10}.txt
  - ls
- you can see the 10 new files that were created

### cp {filename} {destination}

- copies the file to a new directory
  - cp textfile1.txt dev/
