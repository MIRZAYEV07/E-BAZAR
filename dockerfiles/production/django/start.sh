#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset


python /home/app/web/manage.py collectstatic --noinput
python /home/app/web/manage.py migrate

/usr/local/bin/gunicorn config.wsgi:application --bind 0.0.0.0:8000 --max-requests 50 --timeout 360 --workers 8 --threads 8

