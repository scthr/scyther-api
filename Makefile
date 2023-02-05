install:
	pipenv install

install-dev:
	pipenv install --dev


lint:
	pipenv run flake8 scyther_api

format:
	pipenv run black scyther_api
	pipenv run isort scyther_api

run:
	pipenv run python manage.py migrate
	pipenv run python manage.py runserver
