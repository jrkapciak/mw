.DEFAULT_GOAL := all

isort:
	poetry run isort .

black:
	poetry run black .

flake8:
	poetry run flake8 .

pylint:
	poetry run pylint */*.py

bandit:
	poetry run bandit -r .

lint: isort black flake8 pylint bandit

all: lint