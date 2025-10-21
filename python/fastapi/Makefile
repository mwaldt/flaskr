.PHONY: setup run pip-test test clean docker-build docker-run docker-clean lint format pony

VENV := .venv
BIN := $(VENV)/bin
SYSTEM_PYTHON := python3
VENV_PYTHON := $(BIN)/python
APP := $(BIN)/fastapi
PIP := $(BIN)/pip
IMAGE_NAME := flaskr

# Setup and Build
setup: pip

pip: requirements.txt
	$(SYSTEM_PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

run:
	. $(BIN)/activate
	$(APP) dev main.py

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

