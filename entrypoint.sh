#!/bin/sh

poetry run python manage.py migrate --noinput || exit 1
exec "$@"