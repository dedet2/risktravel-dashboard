# Development convenience targets

PYTHON ?= python3

.PHONY: install test run lint clean

install:
	$(PYTHON) -m pip install -r requirements.txt

test:
	$(PYTHON) -m pytest -q

run:
	$(PYTHON) -m uvicorn app.main:app --reload --port 8000

lint:
	flake8 incluu_agents app || true

clean:
	rm -f agent_audit.log