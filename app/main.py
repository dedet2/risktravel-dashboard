"""FastAPI service exposing the agent orchestrator as a REST API.

This service defines a handful of endpoints:

* ``GET /health`` returns a simple JSON indicating the API is running.
* ``GET /agents`` lists all registered agents and the tasks they handle.
* ``GET /marketplace`` exposes a basic marketplace of agents with
  placeholder pricing information. This can be expanded into a
  full‑fledged catalogue.
* ``POST /tasks`` accepts a JSON body containing a ``name`` and
  ``payload``. It validates an API key (if configured) and routes
  the task through the orchestrator. Returns the agent result.

An API key can be configured via the ``API_KEY`` environment variable.
If set, clients must include an ``X‑API‑Key`` header with each
request. If ``API_KEY`` is empty, no authentication is performed.
"""

from __future__ import annotations

import os
from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import Dict, List, Optional

from incluu_agents import (
    Orchestrator,
    SalesAgent,
    SupportAgent,
    AnalyticsAgent,
    JobsAgent,
    HealthAgent,
    LegalAgent,
)

app = FastAPI(title="Incluu Agent Service", version="0.1.0")

# Allow all origins for simplicity; adjust for production deployments
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Instantiate the orchestrator and register agents at startup
orch = Orchestrator()
for agent_cls in [SalesAgent, SupportAgent, AnalyticsAgent, JobsAgent, HealthAgent, LegalAgent]:
    orch.register_agent(agent_cls())


def verify_api_key(x_api_key: Optional[str] = Header(None)) -> None:
    """Dependency to enforce API key verification if configured."""
    expected = os.environ.get("API_KEY")
    if expected:
        if x_api_key != expected:
            raise HTTPException(status_code=401, detail="Invalid API key")


@app.get("/health")
async def health() -> Dict[str, str]:
    """Health check endpoint."""
    return {"status": "ok"}


@app.get("/agents")
async def get_agents() -> List[Dict[str, object]]:
    """List all registered agents and their tasks."""
    agents_list = []
    for agent in orch.registered_agents():
        agents_list.append({
            "name": agent.name,
            "tasks": list(getattr(agent, "tasks", [])),
        })
    return agents_list


@app.get("/marketplace")
async def marketplace() -> List[Dict[str, object]]:
    """Return a simple marketplace description for each agent."""
    marketplace_entries = []
    for agent in orch.registered_agents():
        marketplace_entries.append({
            "name": agent.name,
            "description": f"Agent capable of {', '.join(agent.tasks)}",
            # placeholder pricing: free tier for now
            "pricing": {"tier": "free", "rate": 0.0},
        })
    return marketplace_entries


@app.post("/tasks")
async def post_task(
    body: Dict[str, object],
    api_key: None = Depends(verify_api_key),
) -> JSONResponse:
    """Submit a task to the orchestrator.

    The request body must include:

    * ``name``: The task name (string).
    * ``payload``: A dictionary payload for the task.

    Returns the result produced by the assigned agent.
    """
    name = body.get("name")
    payload = body.get("payload", {})
    if not isinstance(name, str):
        raise HTTPException(status_code=400, detail="Field 'name' must be a string")
    if not isinstance(payload, dict):
        raise HTTPException(status_code=400, detail="Field 'payload' must be an object")
    try:
        result = orch.post_task(name=name, payload=payload)
        return JSONResponse(content=result)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))