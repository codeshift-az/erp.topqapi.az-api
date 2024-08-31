# Define an alias for the specific python version used.
FROM python:3.12.5-slim AS python

# Python build stage
FROM python AS python-build

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONHASHSEED=random
ENV PYTHONFAULTHANDLER=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=.

ARG DJANGO_ENV
ENV DJANGO_ENV=${DJANGO_ENV}

RUN set -xe \
  && apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y --no-install-recommends \
  # dependencies for building Python packages
  build-essential \
  # psycopg2 dependencies
  libpq-dev \
  # For postgres backups
  postgresql-client \
  # For crontab
  cron \
  # Translations dependencies
  gettext \
  # Required for poetry
  curl \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

ENV POETRY_HOME="/opt/poetry"
ENV POETRY_NO_INTERACTION=1
ENV POETRY_VIRTUALENVS_CREATE=false

# Installing `poetry` package manager:
# https://github.com/python-poetry/poetry
RUN curl -sSL 'https://install.python-poetry.org' | python3 -

ENV PATH="$PATH:$POETRY_HOME/bin"

RUN poetry --version

FROM python-build AS python-deps

WORKDIR /app

# Copy only requirements, to cache them in docker layer
COPY ./poetry.lock ./pyproject.toml ./

# Install deps:
RUN poetry run pip install -U pip \
  && poetry install \
  $(if [ "$DJANGO_ENV" = 'prod' ]; then echo '--only main'; fi) \
  --no-interaction --no-ansi

FROM python-deps AS python-run

# We need to run this script as an entry point:
COPY ./docker/app/entrypoint.sh /docker-entrypoint.sh

# Setting up proper permissions:
RUN chmod +x '/docker-entrypoint.sh' \
  # Replacing line separator CRLF with LF for Windows users:
  && sed -i 's/\r$//g' '/docker-entrypoint.sh'

ENTRYPOINT ["/docker-entrypoint.sh"]
