# TopQAPI ERP Project API

This project is a RESTful API for TopQAPI ERP Project.

## Getting Started

### Dependencies

- [Python](https://www.python.org/downloads/) >= 3.12.5
- [Poetry](https://python-poetry.org/docs/#installation) >= 1.8.3
- [Docker](https://docs.docker.com/get-docker/) >= 27.1.1

### Installing

1. Clone the repository

    ```bash
    git clone https://github.com/codeshift-az/erp.topqapi.az-api.git
    ```

2. Install dependencies

    ```bash
    make install
    ```

3. (Optional) Create environment file from example (Required for running project with Docker)

    ```bash
    make cp-env
    ```

### Executing program

1. Run project in local environment

    ```bash
    make run-local
    ```

2. Run project in local environment with Docker

    ```bash
    make run-local-docker
    ```

3. Run project in development environment with Docker

    ```bash
    make run-dev
    ```

4. Run project in production environment with Docker

    ```bash
    make run-prod
    ```
