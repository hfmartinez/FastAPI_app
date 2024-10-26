# FastAPI Todo Application

This is a simple FastAPI application that implements a CRUD (Create, Read, Update, Delete) functionality for managing tasks. It uses MySQL as the database and is containerized using Docker.

## Features

- Create tasks with titles and optional descriptions.
- Retrieve a list of tasks.
- Built using FastAPI and SQLAlchemy.

## Technologies Used

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.7+.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **MySQL**: A popular open-source relational database management system.
- **Docker**: Container platform to package and run applications.

## Prerequisites

- Docker and Docker Compose installed on your machine.
- Basic understanding of Python and RESTful APIs.

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/yourusername/fastapi-todo.git
cd fastapi-todo
```

### Create a `.env` File

Create a `.env` file in the project root directory with the following content:

```bash
MYSQL_ROOT_PASSWORD=root_password
MYSQL_DATABASE=todo_db
MYSQL_USER=user
MYSQL_PASSWORD=password
```

### Build and Run with Docker

Run the following commands to build and start the containers:

```bash
docker-compose up --build
```

### Accessing the Application

- The FastAPI application will be available at `http://localhost:8000`.
- You can access the interactive API documentation at `http://localhost:8000/docs`.

### Stopping the Application

To stop the application, press `Ctrl+C` in the terminal where the containers are running, or use:

```bash
docker-compose down
```

## Usage

### Creating a Task

To create a new task, send a POST request to `/tasks/` with JSON body:

```json
{ "title": "My Task", "description": "This is a sample task." }
```

### Retrieving Tasks

To retrieve all tasks, send a GET request to `/tasks/`.

## Contributing

Feel free to open issues or submit pull requests if you would like to contribute to this project!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
