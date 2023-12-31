.DEFAULT_GOAL := all

isort:
	poetry run isort . $(diff)

black:
	poetry run black . $(diff)

flake8:
	poetry run flake8 .

pylint:
	poetry run pylint */*.py

bandit:
	poetry run bandit -r .

lint: isort black flake8 pylint bandit
all: lint