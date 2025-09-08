# Incluu Agents Platform

This repository contains a self‑contained prototype of an AI‑agent
platform designed to help run your business and personal life.  It
implements a simple orchestrator that brokers tasks to a set of
specialised agents via both a Python interface and an HTTP API.

## Features

* **Modular orchestrator** – Agents register with the orchestrator and
  advertise which tasks they can handle.  Tasks are dispatched to
  appropriate agents.
* **Sales, Support and Analytics agents** – Generate synthetic sales
  leads, respond to canned support queries and compute basic
  statistics over numeric datasets.
* **Life‑management agents** – Perform job searches, look up doctors,
  schedule health appointments, search for lawyers and book legal
  appointments.
* **REST API** – A FastAPI service exposes `/health`, `/agents`,
  `/marketplace` and `/tasks` endpoints.  Requests can optionally be
  protected via an API key set in the `API_KEY` environment variable.
* **Audit logging** – Every task handled by an agent is recorded to
  `agent_audit.log` with timestamp, agent name, task name, payload
  and result.  This makes it easy to trace system behaviour for
  compliance purposes.
* **Marketplace scaffold** – A simple `/marketplace` endpoint returns
  basic metadata and placeholder pricing for each agent.  In a
  production system this would be replaced with a proper catalogue
  and billing integration.
* **Tests included** – Pytest smoke tests exercise each agent and the
  API endpoints to ensure correct behaviour.

## Quickstart

1. **Install dependencies**

   Ensure you have Python 3.11+ installed.  Create a virtual
   environment if desired, then run:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run tests**

   To verify everything works as expected, run the test suite with
   pytest:

   ```bash
   pytest -q
   ```

3. **Start the API**

   Launch the FastAPI service using Uvicorn:

   ```bash
   uvicorn app.main:app --reload --port 8000
   ```

   Visit `http://localhost:8000/docs` for an interactive Swagger UI to
   experiment with the endpoints.

4. **API key (optional)**

   If you wish to secure the API, copy `.env.example` to `.env` and
   set a secret value for `API_KEY`.  Uvicorn will load this variable
   automatically if you use a process manager like `honcho` or set it
   manually in your shell.  Clients must then include the header
   `X‑API‑Key` with the matching value on all requests to `/tasks`.

## Project structure

```
rt_agents_life_package/
├── incluu_agents/          # Python package containing orchestrator and agents
│   ├── __init__.py
│   ├── orchestrator.py     # Orchestrator, task/result definitions, synthetic data
│   └── agents/
│       ├── __init__.py
│       ├── base.py         # Base agent class
│       ├── analytics.py    # AnalyticsAgent
│       ├── health.py       # HealthAgent
│       ├── jobs.py         # JobsAgent
│       ├── legal.py        # LegalAgent
│       ├── sales.py        # SalesAgent
│       └── support.py      # SupportAgent
├── app/
│   └── main.py             # FastAPI app exposing REST endpoints
├── tests/
│   └── test_agents.py      # Pytest smoke tests for agents and API
├── .env.example            # Example environment file for API key
├── Dockerfile              # Container image definition
├── Makefile                # Convenience targets for dev tasks
├── README.md               # This document
└── requirements.txt        # Python dependencies
```

## Extending the platform

To add a new agent:

1. Create a new file in `incluu_agents/agents/` with a class derived
   from `BaseAgent`.  Define a unique `name`, list your supported
   `tasks`, and implement `handle_task`.
2. Register your agent in `app/main.py` by adding the class to the
   `agent_cls` list at startup.
3. Expose any new tasks via the API by sending appropriate requests
   to `/tasks` with `name` set to your new task name and `payload`
   containing the required parameters.
4. Optionally update the `/marketplace` endpoint to include a
   description and pricing for your agent.

## License

This prototype is provided for demonstration purposes only and has
no associated license.  Use at your own risk.