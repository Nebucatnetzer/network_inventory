rm /vagrant/network_inventory/inventory/migrations/*.py
python3 -m venv /vagrant/network_inventory
source /vagrant/network_inventory/bin/activate
pip3 install -r requirements.txt
python3 /vagrant/network_inventory/manage.py makemigrations inventory
python3 /vagrant/network_inventory/manage.py migrate
echo "from django.contrib.auth.models import User; \
      User.objects.filter(email='admin@example.com').delete(); \
      User.objects.create_superuser('admin', 'admin@example.com', 'password')" |
      python3 /vagrant/network_inventory/manage.py shell
python3 /vagrant/network_inventory/manage.py loaddata inventory
