#!/usr/bin/env bash
# exit on error
set -o errexit

#poetry install
pip install -r requirements.txt

python ./university/manage.py collectstatic --no-input
python ./university/manage.py migrate
