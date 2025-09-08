
    .PHONY: dev test run
    dev:
	pip install -r requirements.txt
    test:
	pytest -q
    run:
	uvicorn app.main:app --reload --port 8000
