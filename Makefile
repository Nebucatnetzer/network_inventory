SHELL=/bin/bash

.PHONY: docker

docker:
	docker-compose up

test:
	docker-compose run web pytest network_inventory/ --nomigrations --cov=. --cov-report=html

local:
	python3 -m venv venv
	( \
	source venv/bin/activate; \
	pip3 install -r requirements/local.txt; \
	)

clean:
	rm -rf venv/
	sudo find . \( -name __pycache__ -o -name "*.pyc" \) -delete
	sudo rm -rf htmlcov/
	sudo rm network_inventory/.second_run
	docker-compose down -v --rmi local
