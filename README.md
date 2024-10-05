# Project Name

## Building and Running with Docker

This guide will help you build and run the application using Docker.

### Prerequisites

- Ensure you have Docker installed on your system. You can download it from [Docker's official website](https://www.docker.com/products/docker-desktop).

### Building the Docker Image

1. Open a terminal and navigate to the project directory.

2. Build the Docker image using the following command:

   ```bash
   docker build -t your-image-name .
   ```

   Replace `your-image-name` with a name you want to give to your Docker image.

### Running the Docker Container

1. After building the image, run the Docker container with the following command:

   ```bash
   docker run -p 8000:8000 your-image-name
   ```

   This command maps port 8000 on your host to port 8000 on the Docker container. Adjust the port numbers as needed.

2. Your application should now be running in a Docker container. You can access it by navigating to `http://localhost:8000` in your web browser.

### Stopping the Docker Container

- To stop the running Docker container, press `Ctrl + C` in the terminal where the container is running.

### Additional Notes

- Ensure your application is configured to listen on all interfaces (e.g., `0.0.0.0`) to be accessible from outside the container.
- You can view running containers using `docker ps` and stop them using `docker stop <container_id>`.
