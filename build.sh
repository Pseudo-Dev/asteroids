#! /bin/bash

docker build . -t asteroids

if [[ $(uname) = "Linux" ]]; then
	export IP=$(ip -br -4 addr show | awk -F'/| +' '/UP/ {print $3}' | head -n 1)
elif [[ $(uname) = "Darwin" ]]; then
	export IP=$(ipconfig getifaddr en0)
fi
echo "Host ip set to $IP"