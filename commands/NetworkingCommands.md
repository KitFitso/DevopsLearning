## [To the notes page](../07_Networking.md#networking-commands)

### it has better notes and some examples

- ifconfig
  - this will show you all of the active network interfaces
- ip addr show
  - this will show your own ip address
- ping <ip>
  - this will send packages to the ip and you can see if they have a connection
- tracert <url|ip>
  - you can watch every hop that the request makes to get the ip of that address.
- netstat -antp
  - this will show all of the currently open ports in the machine
- ss -tunlp
  - this is just a little more detailed but the same as above
- nmap
  - _this command can be illegal to run on some sites so please only use it on your own machines for trouble shooting purposes_
  - you might need to install nmap
- dig <url>
  - it will tell you the ip and is used to show if the dns for the server is working or not
- nslookup <url>
  - this is just an older version of dig
- route
  - this will show you the gateways on the routing table
- arp
  - this will list all of the ips/hosts and show you the mac address
- mtr <url>
  - is the same trace but it happens live for you to watch.
- telnet <ip> <port>
  - Telnet is a very primitive serial protocol
