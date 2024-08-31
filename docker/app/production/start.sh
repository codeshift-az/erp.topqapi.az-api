#!/usr/bin/env bash

set -o errexit
set -o nounset
set -o pipefail

# Using `gunicorn` for production, see:
# http://docs.gunicorn.org/en/stable/configure.html

# Check that $DJANGO_ENV is set to "production"
echo "DJANGO_ENV is $DJANGO_ENV"
if [ "$DJANGO_ENV" != 'prod' ]; then
  echo 'Error: DJANGO_ENV is not set to "prod" (production).'
  echo 'Application will not start.'
  exit 1
fi

export DJANGO_ENV

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Copy all environment variables for cron
printenv | grep -Ev 'BASHOPTS|BASH_VERSINFO|EUID|PPID|SHELLOPTS|UID|LANG|PWD|GPG_KEY|_=' >> /etc/environment

# Start cron
service cron start

# Add cron job
echo "Adding cron jobs..."
python manage.py crontab add

# Start gunicorn
echo "Starting gunicorn..."
gunicorn --config python:docker.app.production.config server.wsgi
