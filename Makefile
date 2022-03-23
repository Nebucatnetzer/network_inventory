SHELL=/usr/bin/env bash

.DEFAULT_GOAL := run

.PHONY: run
run: setup
	( \
	find . -name __pycache__ -o -name "*.pyc" -delete; \
	python manage.py runserver; \
	)

.PHONY: setup
setup:
	( \
	docker-compose -f docker-compose-development.yml up -d; \
	if [ -f .second_run ]; then \
		sleep 2; \
		python manage.py collectstatic --noinput; \
		python manage.py makemigrations; \
		python manage.py migrate; \
	else \
		python manage.py collectstatic --noinput; \
		python manage.py makemigrations backups; \
		python manage.py makemigrations computers; \
		python manage.py makemigrations core; \
		python manage.py makemigrations customers; \
		python manage.py makemigrations devices; \
		python manage.py makemigrations licenses; \
		python manage.py makemigrations nets; \
		python manage.py makemigrations softwares; \
		python manage.py makemigrations users; \
		python manage.py makemigrations; \
		python manage.py migrate; \
		python manage.py loaddata backups; \
		python manage.py loaddata computers; \
		python manage.py loaddata core; \
		python manage.py loaddata devices; \
		python manage.py loaddata nets; \
		python manage.py loaddata softwares; \
		python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'password')"; \
		touch .second_run; \
	fi; \
	)

venv:
	nix build .#venv -o venv


.PHONY: clean
clean:
	docker-compose -f docker-compose-development.yml down -v
	find . \( -name __pycache__ -o -name "*.pyc" \) -delete
	rm -rf htmlcov/
	rm -f */migrations/0*.py
	rm .second_run

.PHONY: cleanall
cleanall: clean
	docker-compose  -f docker-compose-development.yml down -v --rmi local
	rm venv

.PHONY: init
init:
	( \
	python manage.py loaddata network_inventory.yaml; \
	)

.PHONY: test
test:
	( \
	pytest -nauto --nomigrations --cov=. --cov-report=html; \
	)

.PHONY: debug
debug:
	( \
	pytest --pdb --nomigrations --cov=. --cov-report=html; \
	)
