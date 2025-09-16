# Incluu Agent Service – Clean Bundle

This repository contains a self‑contained prototype of an AI‑agent
platform. It implements a simple orchestrator and six agents to help
with sales, support, analytics, jobs, health and legal tasks. A
FastAPI service exposes these agents via a REST API.

## Contents

* `incluu_agents/` – Python package containing the orchestrator and
  agents. The orchestrator defines the core routing logic and
  synthetic data helpers. Agents implement specific task handlers.
* `app/main.py` – FastAPI application exposing `/health`, `/agents`,
  `/marketplace` and `/tasks` endpoints. Agents are registered
  automatically at startup.
* `tests/` – Pytest smoke tests verifying registration and basic
  functionality.
* `run_local_check.py` – Simple script to run a quick self‑check
  without requiring pytest.
* `requirements.txt`, `.env.example`, `Dockerfile`, `Makefile` –
  Dependencies and tooling for local development and deployment.

## Quickstart

1. **Install dependencies**

   It’s recommended to use a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Run a self‑check**

   Execute the following to verify the orchestrator and agents:

   ```bash
   python run_local_check.py
   ```

   You should see the list of registered agents and a sample job
   search result.

3. **Launch the API**

   Start the FastAPI service using Uvicorn:

   ```bash
   uvicorn app.main:app --reload --port 8000
   ```

   Then open your browser to `http://127.0.0.1:8000/docs` to explore
   the interactive API documentation. Make sure to include the colon
   between the hostname and port.

4. **API key (optional)**

   If you wish to secure the `/tasks` endpoint, copy `.env.example` to
   `.env` and set the `API_KEY` value. When running the API you
   should include the corresponding `X‑API‑Key` header in your
   requests.

## Usage

* `GET /health` – Check that the service is running.
* `GET /agents` – List all registered agents and the tasks they handle.
* `GET /marketplace` – Return marketplace entries for each agent with
  placeholder pricing. Can be extended into a full catalogue.
* `POST /tasks` – Submit a task to the orchestrator. The request
  body should include:

  ```json
  {
    "name": "job_search",
    "payload": {"count": 3}
  }
  ```

  Replace `name` with any supported task (e.g. `sales_outreach`,
  `generate_report`, `health_search`).

## Deployment options

* **Replit** – For quick testing, create a new Python Replit and
  upload the contents of this repository. Install dependencies and
  run `uvicorn app.main:app --port 8000`. Replit will provide a
  public URL.
* **GitHub** – You can upload this directory to a GitHub repository
  (e.g. `risktravel-dashboard`). Use GitHub’s web interface to add
  files: drag the unzipped contents into the repo root and commit.

### Docker

Build and run the service in a container:

```bash
docker build -t incluu/agent-service .
docker run -p 8000:8000 incluu/agent-service
```

## License

This code is provided for demonstration purposes without warranty.