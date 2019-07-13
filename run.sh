#!/bin/bash
cd network_inventory
python manage.py migrate --settings=$1
python manage.py loaddata inventory --settings=$1
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'password')" --settings=$1
python manage.py runserver 0.0.0.0:8000 --settings=$1