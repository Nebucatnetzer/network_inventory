SHELL=/bin/bash

.PHONY: docker

docker:
	docker-compose up

test:
	docker-compose run web pytest network_inventory/inventory/tests

venv/bin/activate: requirements/local.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip3 install wheel; pip3 install -Ur requirements/local.txt
	touch venv/bin/activate

local:
	python3 -m venv venv
	( \
	source venv/bin/activate; \
	pip3 install -r requirements/local.txt; \
	)

local_test:
	( \
	export DJANGO_SETTINGS_MODULE=network_inventory.settings.local; \
	source venv/bin/activate; \
	cd network_inventory/inventory/tests/; \
	pytest; \
	)

clean:
	rm -f network_inventory/network_inventory/db.sqlite3
	rm -rf venv/
	sudo find . \( -name __pycache__ -o -name "*.pyc" \) -delete
	docker-compose down -v --rmi local
