# Multi-screen distributed Asteroids app

- Set up your networking (see subfolder *networking* and its README)
- To (re)build the Docker image use `docker build . -t asteroids`
- Set the number of replicas by duplicating the app section in *docker-compose.yml* 
- Edit **gridWidth** and **gridHeight** in *app/directions* to match the number of replicas
- Run the system by `docker-compose up`
- Stop a container by clicking in a window or stop all by `Ctrl-c`in the shell
- `docker-compose down --remove-orphans` will clean up any debris
- Remember to eventually use `xhost -` to keep your system secure

*asteroids.proto* contains the Google Protoco Buffers definition of the protocol. You can compile it  with `make` to recreate two Python files in *remote/*. The sed line is required because `protoc` doesn't understand Python package structure.
