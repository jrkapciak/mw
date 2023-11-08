#!/bin/sh

poetry run python manage.py migrate --noinput || exit 1
exec poetry run python manage.py runserver 0.0.0.0:8000 "$@"