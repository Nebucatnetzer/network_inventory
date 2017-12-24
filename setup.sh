rm inventory/migrations/*.py
source bin/activate
pip3 install -r requirements.txt
python3 manage.py makemigrations inventory
python3 manage.py migrate
echo "from django.contrib.auth.models import User; \
      User.objects.filter(email='admin@example.com').delete(); \
      User.objects.create_superuser('admin', 'admin@example.com', 'password')" |
      python3 manage.py shell
