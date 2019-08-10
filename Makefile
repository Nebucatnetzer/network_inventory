SHELL=/bin/bash

.PHONY: docker

docker:
	docker-compose up

test:
	docker-compose run web pytest network_inventory/ --nomigrations --cov=. --cov-report=html


clean:
	rm -rf venv/
	sudo find . \( -name __pycache__ -o -name "*.pyc" \) -delete
	sudo rm -rf htmlcov/
	sudo rm network_inventory/.second_run
	docker-compose down -v --rmi local
