| Command                       | Option  | Arguments | Summary                                                                |
| ----------------------------- | ------- | --------- | ---------------------------------------------------------------------- |
| vagrant init                  |         | boxname   | Creates a new box for the OS.                                          |
| vagrant up                    |         |           | Creates a VM or starts an existing one.                                |
| vagrant ssh                   |         |           | Logs into the running VM.                                              |
| vagrant halt                  |         |           | Stops the VM.                                                          |
| vagrant destroy               |         |           | Deletes the VM.                                                        |
| vagrant box list              |         |           | Lists all boxes installed on the machine.                              |
| vagrant status                |         |           | Shows the status of all VMs.                                           |
| vagrant reload                |         |           | Reboots the VM, equivalent to `halt` then `up`, but faster.            |
|                               |         |           | Useful for applying changes made to the Vagrantfile.                   |
| vagrant global-status         |         |           | Reports the status of all VMs on the machine, useful for multiple VMs. |
| vagrant global-status --prune | --prune |           | Removes any boxes from the list that are not installed or running.     |
