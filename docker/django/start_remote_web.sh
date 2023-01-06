#!/usr/bin/env sh

python /code/manage.py migrate --noinput
python manage.py collectstatic --no-input

python /code/manage.py runserver 0.0.0.0:8000