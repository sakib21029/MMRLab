#!/usr/bin/env bash
# Exit immediately if a command exits with a non-zero status
set -o errexit

pip install -r requirements.txt
python manage.py migrate

echo "ADMIN SCRIPT STARTING"
python create_admin.py

python manage.py collectstatic --no-input