# Multi-screen distributed Asteroids app

- Allow local access to X by `xhost +local:`
- To build the Docker image use `source build.sh`. (The script will also export the host's IP address so you can't use a subshell, thus `source`!)
- Set the number of replicas in *docker-compose.yml*
- Run the system by `docker-compose up --detach` (or `-d` for short)
- Stop a container by clicking in the window
- Remember to eventually use `xhost -local:` to keep your system secure
