#!/bin/bash

[ "x$1" != "xdrop" ] && {
    echo "Use [drop] to completely remove and rebuild database"
} || {
    echo "Removing DB cause drop option"
    rm -f db.sqlite3
}

python3 manage.py makemigrations
python3 manage.py migrate --run-syncdb
