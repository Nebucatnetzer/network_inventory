SHELL=/bin/bash

.PHONY: docker

docker:
	export DJANGO_SETTINGS_MODULE=network_inventory.settings.docker; \
	docker-compose -f docker-compose-development.yml up --build

init:
	export DJANGO_SETTINGS_MODULE=network_inventory.settings.docker; \
	docker-compose -f docker-compose-development.yml run web python manage.py loaddata network_inventory.yaml

test:
	docker-compose -f docker-compose-development.yml run backend pytest -nauto --nomigrations --cov=. --cov-report=html

debug:
	docker-compose -f docker-compose-development.yml run backend pytest --pdb --nomigrations --cov=. --cov-report=html

local:
	python3 -m venv backend/venv
	( \
	source backend/venv/bin/activate; \
	pip3 install -r backend/requirements/local.txt; \
	)

testlocal:
	( \
	source backend/venv/bin/activate; \
	pytest -n 6 --ds=network_inventory.settings.local --nomigrations --cov=. --cov-report=html:backend/htmlcov/ backend/; \
	)


clean:
	docker-compose -f docker-compose-development.yml down -v
	sudo find . \( -name __pycache__ -o -name "*.pyc" \) -delete
	sudo rm -rf backend/htmlcov/
	sudo rm -f backend/*/migrations/0*.py

cleanall:
	docker-compose  -f docker-compose-development.yml down -v --rmi local
	rm -rf backend/venv/
	sudo find . \( -name __pycache__ -o -name "*.pyc" \) -delete
	sudo rm -rf backend/htmlcov/
	sudo rm backend/*/migrations/*.py
