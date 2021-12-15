# Multi-screen distributed Asteroids app

- Allow local access to X by `xhost +local:`
- To (re)build the Docker image use `docker build . -t asteroids`
- Set the number of replicas in *docker-compose.yml* (Doesn't work on Linux, though)
- Run the system by `docker-compose up --detach` (or `-d` for short)
- Stop a container by clicking in the window
- Remember to eventually use `xhost -local:` to keep your system secure
