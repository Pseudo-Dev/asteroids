# Multiple screen distributed Asteroids app

- Allow local access to X by `xhost +local:`
- To build the image use `source build.sh`. (The script will also export the host's IP address so you can't use a subshell, thus `source`!)
- Run the image by `docker-compose up --detach` (or `-d` for short)
- Stop the image by `docker-compose down` or by clicking in the window
- Remember to eventually use `xhost -local:` to keep your system secure
