#! /bin/bash

set -a
source ../.env
set+a

docker network create -d ipvlan \
                      --subnet=$SUBNET \
                      --ip-range=$IPRANGE \
                      --gateway=$GATEWAY \
                      -o parent=$INTERFACE \
                      ether