# docker-pyqt6
Docker files for development of GUI applications with Python 3 + PyQt6, and optionally with PostgreSQL.

## Tags
- Python
- PyQt6
- Docker
- GUI
- Linux
- Development
- Containerization
- Ubuntu
- Application Development

## Docker Hub Repository
Visit the [docker-pyqt6 Docker Hub Repository](https://hub.docker.com/repository/docker/dasycarpum/pyqt6/general) for more details and image downloads.

## How to use v1.0.0 on Linux
*Tested on Ubuntu 22.04*

### Prerequisites
- Docker and Docker Compose installed on your system.

### Testing the Application
You can test if everything works with a small testing application. Follow these steps:

1. **Allow X Server Access**:
    - Run `xhost +local:docker-app-1` to allow access to the X server from the Docker container.
    - `docker-app-1` is the name of your Docker container.
    - To revert this permission, use `xhost -local:docker-app-1`.

2. **Start the Docker Container**:
    - Navigate to the directory containing your `docker-compose.yml`.
    - Run `docker-compose up -d` to start the container.

You should see a window similar to this :

![Capture d’écran du 2023-11-26 17-07-38](https://github.com/dasycarpum/docker-pyqt6/assets/35745289/92505328-6280-4ce4-9e2e-f321f9460523)

### Support and Contributions
For support, questions, or contributions, please submit an issue or pull request on GitHub.





