#! /bin/bash

hostname -I
# ping -c 5 172.16.0.3
# ping -c 5 172.16.0.4
# ping -c 5 172.16.0.247
/usr/sbin/syslog-ng --no-caps
/usr/local/bin/python main.py