| Command      | Option | Arguments                | Summary                                                                     |
| ------------ | ------ | ------------------------ | --------------------------------------------------------------------------- |
| cd           |        |                          | Moves the user around directories.                                          |
| cd           |        | -                        | Returns to the home directory.                                              |
| cd           |        | ~                        | Same as `cd -`, returns to the home directory.                              |
| cd           |        | ..                       | Moves back one directory level.                                             |
| cd           |        | {dir name}               | Tries to move up one level to that directory.                               |
| cd           |        | /home/{user}             | Uses an absolute path to move directly to a directory.                      |
| cp           |        | {filename} {destination} | Copies a file to a new directory. Ensure the destination ends with `/`.     |
| cp           | -r     |                          | Copies entire directories recursively.                                      |
| exit         |        |                          | Logs out of the root user or virtual machine.                               |
| free         | -m     |                          | Displays available memory in megabytes.                                     |
| history      |        |                          | Lists all commands used in the current session.                             |
| ip addr show |        |                          | Displays network interface details (similar to `ipconfig` on Windows).      |
| ls           |        |                          | Lists all files and directories in the current directory.                   |
| ls           | -l     |                          | Displays a detailed list including permissions, timestamps, and file sizes. |
| ls           |        | {dir}                    | Lists files of a specified directory.                                       |
| mkdir        |        | {dirname/s}              | Creates a new directory in the current location.                            |
| mkdir        |        | {dirname{n..n+}}         | Creates multiple directories using a range.                                 |
| mv           |        | {file} {file or dir}     | Moves or renames a file.                                                    |
| mv           |        | \_                       | Moves all files of a certain type (e.g., `mv _.txt dev/`).                  |
| pwd          |        |                          | Prints the present working directory.                                       |
| rm           |        | {file or directory}      | Removes a file.                                                             |
| rm           | -r     |                          | Removes a directory and its contents recursively.                           |
| rm           | -rf    | \*                       | [DANGEROUS] Removes everything with no confirmation.                        |
| sudo         | -i     |                          | Switches from the current user to root user with higher permissions.        |
| touch        |        | {filename}               | Creates an empty file.                                                      |
| touch        |        | {filename{1..n}}         | Creates multiple files using a range (e.g., `touch file{1..10}.txt`).       |
| uptime       |        |                          | Displays system uptime and load averages.                                   |
| whoami       |        |                          | Prints the username of the current user.                                    |
| {any}        | --help |                          | Displays help information about a command.                                  |
