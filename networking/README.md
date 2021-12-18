# Asteroids networking

To get containers on your real network you will need to set up a Docker IPvLAN. The command is in *network.sh*, but you will need to edit it first to match your network. Change all the addresses to match yours, probably 192.168.0.xxx.

The *ip-range* is the range where Docker will assign IP addresses. DHCP is not used!! Docker will assign the addresses blindly, so pick a range that is not used by other devices on your network. xx.xx.xx.128/27 means that addresses 129 to 159 will be used starting from the lower bound.

The *parent* is the interface the host is connected to network. Use wired interface if available, but wireless should also work. Check the actual interface name with `ifconfig`.

*network.sh* will create a permanent network *ether* which you can eventually delete with ´docker network rm ether`.

In addition you will need to set an environment variable IP with the ip address of your X Server, probably the Docker host itself. All X traffic goes through the network so use an IP in the same network as your in your IPvLAN. You can either `export IP=192.168.0.xxx` in every new shell session or create a file *.env* with text IP=IP=192.168.0.xxx in it.

You will need to allow access to your X server from the network. The quickest way is `xhost +` which will disable all security. Use it in a trusted network only. Restore security with `xhost -`.
