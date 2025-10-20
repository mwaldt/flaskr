.PHONY: setup run pip-test test clean docker-build docker-run docker-clean lint format pony

VENV := .venv
BIN := $(VENV)/bin
PYTHON := python3
FLASK := $(BIN)/flask
PIP := $(BIN)/pip
IMAGE_NAME := flaskr

setup: pip init-db

pip: requirements.txt
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -e . -r requirements.txt

init-db:
	$(FLASK) --app flaskr init-db

run:
	. $(BIN)/activate
	$(FLASK) --app flaskr run --debug
	# $(BIN)/bin/python main.py

pip-test: pip requirements-tests.txt
	$(PIP) install -r requirements-tests.txt

test: pip-test
	$(BIN)/pytest

coverage:
	$(BIN)/coverage run -m pytest

coverage-report:
	$(BIN)/coverage report

coverage-html:
	$(BIN)/coverage html

clean:
	rm -rf $(VENV)

