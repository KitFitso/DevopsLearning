- ip addr show
  - basically ipconfig

---

- whoami
  - shows the user name of the person using this machine

---

- pwd
  - shows where you were current working or present working directory

---

- sudo -i
  - switches from working user to root user

---

- exit
  - log out of the root user or VM

---

- cd
  - this moves the user around directories
  - cd .. - is back 1 level
  - cd {dir name} - will try to move up 1 level to that dir
  - cd - alone this will return you to your home dir
  - you can also type out a whole route /home/{user} to move directly to that dir
  - tab will show you possible dirs or auto fill if there is only 1

---

- uptime
  - shows how long this session has been active

---

- free -m
  - shows how much free memory you have

---

- mkdir {dirname/s}
  - creates a new directory in the current directory
  - can create many if seperated by spaces

---

- touch {filename}
  - creates a new empty file
  - can create an array of files if you use ..
    - touch devfile{1..10}.txt

---

- cp {filename} {destination}
  - copies a file to a new directory
