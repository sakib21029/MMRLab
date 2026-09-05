#!/usr/bin/env bash
set -o errexit

cd mmr_lab
pip install -r requirements.txt
python manage.py migrate

echo "ADMIN SCRIPT STARTING"
python create_admin.py

python manage.py collectstatic --no-input
