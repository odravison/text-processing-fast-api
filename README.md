
# Text Processing FastAPI

This project is a text processing application using [FastAPI](https://fastapi.tiangolo.com/), focusing on using background tasks. The goal is to provide an API for asynchronous text processing.

## Features

- Asynchronous text processing using FastAPI Background Tasks.
- PostgreSQL integration for data storage.
- Dockerized with Docker Compose orchestration.

## Prerequisites

- [Docker](https://www.docker.com/) installed.
- [Docker Compose](https://docs.docker.com/compose/) installed.

## Setup

1. Clone this repository:

   ```bash
   git clone https://github.com/odravison/text-processing-fast-api.git
   ```

2. Navigate to the project directory:

   ```bash
   cd text-processing-fast-api
   ```

## Usage

The project uses a `Makefile` to simplify common operations. The available main commands are:

- **`make up`**: Build the Docker image and start the containers in detached mode.

  ```bash
  make up
  ```

- **`make down`**: Stop and remove the containers.

  ```bash
  make down
  ```

- **`make restart`**: Restart the containers.

  ```bash
  make restart
  ```

- **`make logs`**: Tail the logs of the containers.

  ```bash
  make logs
  ```

- **`make clean`**: Remove unused containers, volumes, and images.

  ```bash
  make clean
  ```

- **`make check-lint`**: Run linting checks on the code.

  ```bash
  make check-lint
  ```

- **`make apply-lint`**: Apply formatting and lint fixes to the code.

  ```bash
  make apply-lint
  ```

## Project Structure

The main structure of the project is as follows:

```
text-processing-fast-api/
├── src/
│   ├── main.py
│   ├── ...
├── tests/
│   ├── test_main.py
│   ├── ...
├── Dockerfile
├── docker-compose.yml
├── Makefile
└── README.md
```

- **`src/`**: Contains the source code for the application.
- **`tests/`**: Contains automated tests.
- **`Dockerfile`**: Defines the Docker image for the application.
- **`docker-compose.yml`**: Defines Docker services and their configurations.
- **`Makefile`**: Contains commands to simplify common operations.
- **`README.md`**: This file, with information about the project.

## Testing

To test you should execute `make up`and then call the following cURL command (adjusting as needed):

```bash
curl -X POST "http://localhost:8000/v1/text/" -H "Content-Type: application/json" -d '{"text":"your_text"}'
```

## Roadmap

1.  [Add Unit of Work Pattern](https://docs.sqlalchemy.org/en/20/tutorial/orm_data_manipulation.html#tutorial-inserting-orm) to support atomic endpoint calls
2. Add logs among the code
3. Add obeservability support
4. Unit and integration tests