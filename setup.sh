rm network_inventory/inventory/migrations/*.py
python3 -m venv network_inventory
source network_inventory/bin/activate
pip3 install -r requirements.txt
python3 network_inventory/manage.py makemigrations inventory
python3 network_inventory/manage.py migrate
echo "from django.contrib.auth.models import User; \
      User.objects.filter(email='admin@example.com').delete(); \
      User.objects.create_superuser('admin', 'admin@example.com', 'password')" |
      python3 network_inventory/manage.py shell
python3 network_inventory/manage.py loaddata inventory
