#!/bin/bash

rm ./ywsapp/migrations/0001_initial.py
rm db.sqlite3
python3 manage.py makemigrations
python3 manage.py migrate
