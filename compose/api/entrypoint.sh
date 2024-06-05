#!/bin/sh

echo "Waiting for PostgreSQL..."
while ! nc -z postgis 5432; do
  sleep 1
done

echo "PostgreSQL is up and running"

# Run database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start the application
exec gunicorn --bind 0.0.0.0:8000 bootcamp_m.wsgi:application