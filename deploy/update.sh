#!/usr/bin/env bash

set -e

PROJECT_BASE_PATH='/usr/local/apps/profiles-rest-api'

git pull
$PROJECT_BASE_PATH/env/bin/python manage.py migrate
supervisorctl restart api

echo "DONE! :)"