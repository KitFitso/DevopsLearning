## [To the notes page - setup](../02_VMSetup.md)

## [To the notes page - servers](../04_Servers.md)

### it has better notes and some examples

- vagrant init boxname
  - creates a new box for OS
- vagrant up
  - creates VM or if it exists start up
- vagrant ssh
  - to log in
- vagrant halt
  - to stop vm
- vagrant destroy
  - deletes vm
- vagrant box list
  - lists all boxes installed on the machine
- vagrant status
  - shows the status of all vms
- vagrant reload [--provision]
  - reboots the vm. this is the same of halt then up, just faster
  - useful if you made any changes to the vagrant file, it will apply them
  - you can force the provision by adding --provision at the end
- vagrant global-status
  - reports the status of all vms on the machine. if you have more than 1 running
- vagrant global-status --prune
  - removes any boxes from the list that are not installed or running
- vagrant box list
  - lists every virtual box that you have installed on your machine
