#!/bin/sh

poetry run python manage.py migrate --noinput || exit 1
exec poetry run gunicorn -b 0.0.0.0:8000 config.wsgi:application "$@"