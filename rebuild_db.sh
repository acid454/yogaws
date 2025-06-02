#!/bin/bash

rm -f ./ywsapp/migrations/0001_initial.py
rm -f db.sqlite3
python3 manage.py makemigrations
python3 manage.py migrate
