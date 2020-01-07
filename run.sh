#!/bin/bash
if [ -f ./.second_run ]; then
    sleep 2
    python manage.py makemigrations
    python manage.py migrate
else
    python manage.py makemigrations core
    python manage.py makemigrations customer
    python manage.py makemigrations inventory
    python manage.py makemigrations
    python manage.py migrate
    python manage.py loaddata core
    python manage.py loaddata inventory
    python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'password')"
    touch .second_run
fi
python manage.py runserver 0.0.0.0:8000
