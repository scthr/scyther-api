install:
	pipenv install

install-dev:
	pipenv install --dev


lint:
	flake8 scyther_api
	mypy scyther_api

format:
	black scyther_api
	isort scyther_api

run:
	python manage.py migrate
	python manage.py runserver

