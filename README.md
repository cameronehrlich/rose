# Project Name

## Building and Running with Docker

1. Open a terminal and navigate to the project directory.

2. Build the application using Docker Compose with the following command:

   ```bash
   docker-compose build
   ```

### Prerequisites

- Ensure you have Docker installed on your system. You can download it from [Docker's official website](https://www.docker.com/products/docker-desktop).

### Running the Application with Docker Compose

1. Open a terminal and navigate to the project directory.

2. Start the application using Docker Compose with the following command:

   ```bash
   docker-compose up --build
   ```

   This command will build the image if it hasn't been built yet and start the application, mapping port 8000 on your host to port 8000 on the Docker container.

3. Your application should now be running in a Docker container. You can access it by navigating to `http://localhost:8000` in your web browser.

### Stopping the Application

- To stop the application, press `Ctrl + C` in the terminal where Docker Compose is running, or run:

  ```bash
  docker-compose down
  ```

  This command stops and removes the containers defined in the `docker-compose.yml`.

### Additional Notes

- Ensure your application is configured to listen on all interfaces (e.g., `0.0.0.0`) to be accessible from outside the container.
- You can view running containers using `docker ps` and stop them using `docker stop <container_id>`.
