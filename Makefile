pip-install-dev:
	pip install --upgrade pip pip-tools
	pip-sync requirements.txt requirements-dev.txt

pip-install:
	pip install --upgrade pip pip-tools
	pip-sync requirements.txt

pip-update:
	pip install --upgrade pip pip-tools
	pip-compile requirements.in
	pip-compile requirements-dev.in
	pip-sync requirements.txt requirements-dev.txt

lint:
	flake8 scyther_api
	mypy scyther_api

format:
	black scyther_api
	isort scyther_api

run:
	python manage.py migrate
	python manage.py runserver

