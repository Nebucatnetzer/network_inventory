SHELL=/usr/bin/env bash

.PHONY: docker

docker:
	export DJANGO_SETTINGS_MODULE=network_inventory.settings.docker; \
	docker-compose -f docker-compose-development.yml up

init:
	export DJANGO_SETTINGS_MODULE=network_inventory.settings.docker; \
	docker-compose -f docker-compose-development.yml run web python manage.py loaddata network_inventory.yaml

test:
	docker-compose -f docker-compose-development.yml run web pytest -nauto --nomigrations --cov=. --cov-report=html

debug:
	docker-compose -f docker-compose-development.yml run web pytest --pdb --nomigrations --cov=. --cov-report=html

local:
	python3 -m venv venv
	( \
	source venv/bin/activate; \
	pip3 install -r requirements/local.txt; \
	)

testlocal:
	( \
	source venv/bin/activate; \
	pytest -n6 --ds=network_inventory.settings.local --nomigrations  --cov=. --cov-report=html; \
	)


clean:
	docker-compose -f docker-compose-development.yml down -v
	sudo find . \( -name __pycache__ -o -name "*.pyc" \) -delete
	sudo rm -rf htmlcov/
	sudo rm -f */migrations/0*.py

cleanall:
	docker-compose  -f docker-compose-development.yml down -v --rmi local
	rm -rf venv/
	sudo find . \( -name __pycache__ -o -name "*.pyc" \) -delete
	sudo rm -rf htmlcov/
	sudo rm */migrations/*.py
