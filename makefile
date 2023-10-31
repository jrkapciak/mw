.DEFAULT_GOAL := all

isort:
	poetry run isort .

black:
	poetry run black .

flake8:
	poetry run flake8 .

pylint:
	poetry run pylint src

bandit:
	poetry run bandit -r .

lint: isort black flake8 pylint

tests: test

all: lint tests