.DEFAULT_GOAL := help

ENV ?=

ifneq (,$(wildcard ./config/.env))
    include config/.env
    export
endif

.PHONE: help
help:
	@echo " Please use 'make <target>' where <target> is one of: "
	@echo " ------------------------- Setup commands ---------------------------- "
	@echo " help                        to show this message"
	@echo " install                     to install dependencies"
	@echo " makeenv                     to create an .env file with interactive prompt"
	@echo " lint                        to lint code with pre-commit hooks"
	@echo " ------------------------- Quick commands ---------------------------- "
	@echo " run-local									  to run Django server locally"
	@echo " run-dev										  to run Django server in development mode"
	@echo " run-prod									  to run Django server in production mode"
	@echo " logs											  to show Docker logs"
	@echo " shell										    to run shell in Django Docker container"
	@echo " ------------------------- Django commands --------------------------- "
	@echo " django-runserver            to run Django server"
	@echo " django-migrate              to run Django migrations"
	@echo " django-makemigrations       to make Django migrations"
	@echo " django-createsuperuser      to create Django superuser"
	@echo " django-shell                to run Django shell"
	@echo " django-makemessages         to make Django messages"
	@echo " django-compilemessages      to compile Django messages"
	@echo " django-backup							  to backup Django database and media files"
	@echo " ------------------------- Docker commands --------------------------- "
	@echo " docker-help 							  to show help for environment and service"
	@echo " docker-build                to build Docker images"
	@echo " docker-up						        to start Docker containers"
	@echo " docker-down                 to stop Docker containers"
	@echo " docker-down-v               to stop Docker containers and remove volumes"
	@echo " docker-start                to start Docker containers"
	@echo " docker-stop                 to stop Docker containers"
	@echo " docker-restart              to restart Docker containers"
	@echo " docker-logs                 to show Docker logs"
	@echo " --------------------------------------------------------------------- "

# ------------------------- Setup commands ---------------------------- #

.PHONY: install
install:
	@echo "SETUP: Installing dependencies"
	poetry install
	@echo "SETUP: Installing pre-commit hooks"
	poetry run pre-commit install

.PHONY: makeenv
makeenv:
	poetry run python manage.py makeenv

.PHONY: lint
lint:
	@echo "SETUP: Linting code with pre-commit hooks"
	poetry run pre-commit run --all-files

# ------------------------- Quick commands ---------------------------- #

.PHONY: run-local
run-local: django-runserver

.PHONY: run-dev
run-dev: ENV=dev
run-dev: docker-up docker-logs

.PHONY: run-prod
run-prod: ENV=prod
run-prod: docker-up docker-logs

.PHONY: logs
logs: docker-logs

.PHONY: shell
shell: svc=app
shell: shell=bash
shell: docker-shell

# ------------------------- Django commands --------------------------- #

python-run = poetry run python

app ?=

ifneq ($(ENV), local)
	python-run = $(docker-compose) exec app python
endif

.PHONY: check-env
check-env:
ifeq (,$(wildcard ./config/.env))
	@echo "ERROR: .env file is missing. Please run makeenv command to create it"
	@exit 1
endif

.PHONY: django-runserver
django-runserver: check-env
	@echo "DJANGO: Running Django server"
	$(python-run) manage.py runserver ${DJANGO_PORT}

.PHONY: django-migrate
django-migrate: check-env
	@echo "DJANGO: Running Django migrations"
	$(python-run) manage.py migrate $(app)

.PHONY: django-makemigrations
django-makemigrations: check-env
	@echo "DJANGO: Making Django migrations"
	$(python-run) manage.py makemigrations $(app)

.PHONY: django-createsuperuser
django-createsuperuser: check-env
	@echo "DJANGO: Creating Django superuser"
	$(python-run) manage.py createsuperuser

.PHONY: django-shell
django-shell: check-env
	@echo "DJANGO: Running Django shell"
	$(python-run) manage.py shell

.PHONY: django-makemessages
django-makemessages: check-env
	@echo "DJANGO: Making Django messages"
	$(python-run) manage.py makemessages -l en

.PHONY: django-compilemessages
django-compilemessages: check-env
	@echo "DJANGO: Compiling Django messages"
	$(python-run) manage.py compilemessages --ignore site-packages

.PHONY: django-backup
django-backup: check-env
	@echo "DJANGO: Backing up Django database and media files"
	$(python-run) manage.py backup

# ------------------------- Docker commands --------------------------- #

args = -f docker-compose.yml --env-file config/.env --project-name ${PROJECT_NAME}

dev = -f docker/docker-compose.dev.yml
prod = -f docker/docker-compose.prod.yml

svc ?=
shell ?= sh

docker-compose = docker compose $(args) $($(ENV))

.PHONY: check-local
check-local: check-env
ifeq ($(ENV), local)
	@echo "ERROR: You can't run this command in local environment"
	@exit 1
endif

.PHONY: docker-help
docker-help:
	@echo "--------------------------------  Environment  ---------------------------------"
	@echo "To run the command for a specific environment run 'make ENV=<env> <target>'"
	@echo "or set ENV variable to <env> and run 'make <target>', where <env> is:"
	@echo "local:    the app in local mode without Docker (the docker commands won't work)"
	@echo "dev:      the app in development mode (essential + django in development mode)"
	@echo "prod:     the app in production mode (essential + django in production mode)"
	@echo "----------------------------------  Service  -----------------------------------"
	@echo "To run the command for a specific service run 'make svc=<service> <target>'"
	@echo "where <service> is one of the services in docker compose file"
	@echo "--------------------------------------------------------------------------------"

.PHONY: docker-build
docker-build: check-local
	@echo "DOCKER: Building Docker images"
	$(docker-compose) build $(svc)

.PHONY: docker-up
docker-up: check-local
	@echo "DOCKER: Starting Docker containers"
	$(docker-compose) up -d $(svc)

.PHONY: docker-down
docker-down: check-local
	@echo "DOCKER: Stopping Docker containers"
	$(docker-compose) down $(svc)

.PHONY: docker-down-v
docker-down-v: check-local
	@echo "DOCKER: Stopping Docker containers"
	$(docker-compose) down $(svc) -v

.PHONY: docker-start
docker-start: check-local
	@echo "DOCKER: Starting Docker containers"
	$(docker-compose) start $(svc)

.PHONY: docker-stop
docker-stop: check-local
	@echo "DOCKER: Stopping Docker containers"
	$(docker-compose) stop $(svc)

.PHONY: docker-restart
docker-restart: check-local
	@echo "DOCKER: Restarting Docker containers"
	$(docker-compose) restart $(svc)

.PHONY: docker-logs
docker-logs: check-local
	@echo "DOCKER: Showing Docker logs"
	$(docker-compose) logs -f $(svc)

.PHONY: docker-shell
docker-shell: check-local
	@echo "DOCKER: Running shell in Docker container"
	$(docker-compose) exec $(svc) $(shell)

# --------------------------------------------------------------------- #
