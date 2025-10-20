.PHONY: setup run pip-test test clean docker-build docker-run docker-clean lint format pony

VENV := .venv
BIN := $(VENV)/bin
SYSTEM_PYTHON := python3
VENV_PYTHON := $(BIN)/python
FLASK := $(BIN)/flask
PIP := $(BIN)/pip
IMAGE_NAME := flaskr

# Setup and Build
setup: pip init-db

pip: requirements.txt
	$(SYSTEM_PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -e . -r requirements.txt

init-db:
	$(FLASK) --app flaskr init-db

wheel-build:
	$(PIP) install build
	$(VENV_PYTHON) -m build --wheel

wheel-steup: init-db
	$(PIP) install flask-1.0.0-py3-none-any-.whl

# uwsgi via waitress
serve:
	$(BIN)/waitress-serve --call 'flaskr:create_app'

run:
	. $(BIN)/activate
	$(FLASK) --app flaskr run --debug
	# $(BIN)/bin/python main.py


# Testing
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

