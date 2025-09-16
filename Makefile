.PHONY: install test run check

install:
	pip install -r requirements.txt

test:
	pytest -q

run:
	uvicorn app.main:app --reload --port 8000

check:
	python run_local_check.py