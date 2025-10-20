.PHONY: setup run pip-test test clean docker-build docker-run docker-clean lint format pony

VENV := .venv
BIN := $(VENV)/bin
PYTHON := python3
PIP := $(BIN)/pip
IMAGE_NAME := flaskr

setup: pip

pip: requirements.txt
	$(PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

run: pip
	. $(BIN)/activate
	.venv/bin/flask --app flaskr run --debug
	# $(BIN)/bin/python main.py

pip-test: pip requirements-tests.txt
	$(PIP) install -r requirements-tests.txt

test: pip-test
	$(BIN)/pytest

clean:
	rm -rf $(VENV)

