.PHONY: setup test clean

VENV := .venv
BIN := $(VENV)/bin
SYSTEM_PYTHON := python3
PIP := $(BIN)/pip

# Setup and Build
setup: pip

pip: requirements.txt
	$(SYSTEM_PYTHON) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install -e . -r requirements.txt

test:
	$(BIN)/pytest

coverage:
	$(BIN)/coverage run -m pytest

coverage-report:
	$(BIN)/coverage report

coverage-html:
	$(BIN)/coverage html

clean:
	rm -rf $(VENV)

