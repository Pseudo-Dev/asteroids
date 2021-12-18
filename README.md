# Multi-screen distributed Asteroids app

- Set up your networking (see subfolder *networking*)
- To (re)build the Docker image use `docker build . -t asteroids`
- Set the number of replicas by duplicating the app section in *docker-compose.yml*
- Run the system by `docker-compose up`
- Stop a container by clicking in a window or stop all by `Ctrl-c`in the shell
- `docker-compose down --remove-orphans` will clean up any debris
- Remember to eventually use `xhost -` to keep your system secure
