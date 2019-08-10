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

clean:
	rm -rf venv/
	sudo find . \( -name __pycache__ -o -name "*.pyc" \) -delete
	sudo rm -rf htmlcov/
	sudo rm network_inventory/.second_run
	docker-compose down -v --rmi local
