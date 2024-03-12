# Health App

## Introduction
This project is a full-stack web application named "Health App". It's designed to provide users with visual interface to interract with database, containing information about patients, appointments and prescriptions. The backend is built with Python, handling data processing and server-side logic. The frontend is developed using Vue.js, providing a dynamic and responsive user interface. Docker is used for containerization, ensuring that the application runs consistently across different computing environments. The `docker-compose.yml` file is used to define and run the application's services.

## Project Structure
- `backend/`: This directory contains the server-side code written in Python. Key files include `api.py` (handles API routes), `schema.py` (defines the database schema), and `database.py` (manages database connections and operations).
- `frontend/`: This directory contains the client-side code written in Vue.js. Key files include `App.vue` (the root Vue component) and `main.js` (the entry point of the application).
- `docker-compose.yml`: This file is used by Docker Compose to orchestrate the application's services. It defines how the different parts of the application (frontend, backend, database, etc.) interact with each other.

## Getting Started

### Prerequisites

1. Install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) on your machine.

### Installation

1. Clone the repository to your local machine.
    ```sh
    git clone https://github.com/ProcrastinatorMuffin/VUE-health-app
    ```

2. Navigate to the project directory.
    ```sh
    cd VUE-health-app
    ```

3. Build and run the Docker containers using Docker Compose.
    ```sh
    docker-compose up --build
    ```

The application should now be running on your local machine. The frontend should be accessible at `http://localhost:5173` and the backend at `http://localhost:3000`.

## Deployment

To deploy the application, you can use the same Docker Compose command. However, you'll need to set up a Docker environment on your server. Once that's done, you can clone the repository on your server and run the `docker-compose up --build` command to start the application.

## Contributing

You are welcome to contribute to the project. 

### How to Contribute

1. Fork the repository to your own GitHub account.
2. Clone the project to your machine.
3. Create a branch in your local repository.
4. Make your changes and commit them to your local repository.
5. Push your changes to your GitHub repository.
6. Submit a pull request to the main project repository. Please provide a complete and thorough description explaining the changes, why you made them, and how they are expected to solve the stated problem.

## License

This project is licensed under the MIT License. For details, please see the [LICENSE](LICENSE.md) file.
