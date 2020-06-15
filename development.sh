#!/bin/bash
if [ -f ./.second_run ]; then
    sleep 2
    python manage.py collectstatic --noinput
    python manage.py makemigrations
    python manage.py migrate
else
    python manage.py collectstatic --noinput
    python manage.py makemigrations backups
    python manage.py makemigrations computers
    python manage.py makemigrations core
    python manage.py makemigrations customers
    python manage.py makemigrations devices
    python manage.py makemigrations licenses
    python manage.py makemigrations nets
    python manage.py makemigrations softwares
    python manage.py makemigrations users
    python manage.py makemigrations
    python manage.py migrate
    python manage.py loaddata backups
    python manage.py loaddata computers
    python manage.py loaddata core
    python manage.py loaddata devices
    python manage.py loaddata nets
    python manage.py loaddata softwares
    python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'password')"
    python manage.py loaddata network_inventory.yaml
    touch .second_run
fi
python manage.py runserver 0.0.0.0:8000
