docker-compose run web python manage.py migrate
docker-compose run web python manage.py loaddata inventory
docker-compose run web ./manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'password')"