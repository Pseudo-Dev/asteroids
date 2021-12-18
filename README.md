# Multi-screen distributed Asteroids app

- Set up your [networking](https:networking/networking)
- To (re)build the Docker image use `docker build . -t asteroids`
- Set the number of replicas by duplicating the app section in *docker-compose.yml*
- Run the system by `docker-compose up`
- Stop a container by clicking in a window or stop all by `Ctrl-c`in the shell
- Remember to eventually use `xhost -` to keep your system secure
