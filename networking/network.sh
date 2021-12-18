#! /bin/sh

docker network create -d ipvlan \
                      --subnet=172.16.0.0/24 \
                      --ip-range=172.16.0.128/27 \
                      --gateway=172.16.0.1 \
                      -o parent=eth0 \
                      ether