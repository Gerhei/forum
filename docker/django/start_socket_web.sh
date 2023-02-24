#!/usr/bin/env sh

python /code/manage.py migrate --noinput
python manage.py collectstatic --no-input

/usr/local/bin/gunicorn src.wsgi -w 4 --bind=unix:/django/site.sock --bind=0.0.0.0:8000 --timeout=3600