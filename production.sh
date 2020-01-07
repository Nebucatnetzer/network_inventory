#!/bin/bash
if [ -f ./.second_run ]; then
    python manage.py makemigrations
    python manage.py migrate
else
    python manage.py makemigrations inventory
    python manage.py makemigrations
    python manage.py migrate
    python manage.py loaddata inventory
    python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'password')"
    touch .second_run
fi

gunicorn network_inventory.wsgi:application --bind 0.0.0.0:8000 --workers 3
