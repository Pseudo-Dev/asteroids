# Asteroids networking

To make the containers appear on your real network you will need to set up a Docker IPvLAN. The command is in *networking/network.sh*, but you will need to create a *.env* first to match your network. Place the *.env* file at the root (not in */networking*)!. Mine looks like this:

    IP=172.16.0.247
    INTERFACE=enp0s31f6
    SUBNET=172.16.0.0/24
    IPRANGE=172.16.0.128/28
    GATEWAY=172.16.0.1

Change all addresses to match your network, probably 192.168.0.xxx.

*IP* is the ip address of your X Server where you want to show the animation, probably the Docker host itself. All X traffic goes through the network so it is better to use an IP in the same network as your IPvLAN.

You will also need to allow access to your X server from the network. The quickest way is `xhost +` which will disable all security. Use it in a trusted network only. (Restore security with `xhost -`.)

*INTERFACE* is the name of the interface the host is connected to network. Use wired interface if available, but wireless should also work. Check the actual interface name with `ifconfig`.

The *IPRANGE* is the range where Docker will assign IP addresses. DHCP is not used!! Docker will assign the addresses blindly, so pick a range that is not used by other devices on your network. xx.xx.xx.128/28 means that addresses 128 to 143 will be used starting from the lower bound.

*network.sh* will create a permanent Docker network *ether* so you will only do this once. You can delete the network afterwards with ´docker network rm ether`.

## Python configuration

You will also need to make a similar configuration in *remote/config.py*.
