"""FastAPI service exposing the Incluu agent orchestrator as REST endpoints."""

from __future__ import annotations

import os
from typing import Dict, Any, List, Optional

from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from incluu_agents import (
    Orchestrator,
    SalesAgent,
    SupportAgent,
    AnalyticsAgent,
    JobsAgent,
    HealthAgent,
    LegalAgent,
)

app = FastAPI(title="Incluu Agent Service", version="0.2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Instantiate orchestrator and register all agents
orch = Orchestrator()
for agent_cls in [SalesAgent, SupportAgent, AnalyticsAgent, JobsAgent, HealthAgent, LegalAgent]:
    orch.register_agent(agent_cls())

API_KEY = os.environ.get("API_KEY", "")  # optional API key

def verify_api_key(x_api_key: Optional[str] = Header(None)) -> None:
    if API_KEY and x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")


@app.get("/health")
async def health() -> Dict[str, str]:
    """Health check endpoint."""
    return {"status": "ok"}


@app.get("/agents")
async def get_agents() -> List[Dict[str, Any]]:
    """Return a list of all registered agents and their tasks."""
    agents = []
    for agent in orch.registered_agents():
        agents.append({"name": agent.name, "tasks": list(agent.tasks)})
    return agents


@app.get("/marketplace")
async def marketplace() -> List[Dict[str, Any]]:
    """Return marketplace entries for each agent with placeholder pricing."""
    entries = []
    for agent in orch.registered_agents():
        entries.append({
            "name": agent.name,
            "description": f"Agent capable of {', '.join(agent.tasks)}",
            "pricing": {"tier": "free", "rate": 0.0},
        })
    return entries


@app.post("/tasks")
async def post_task(
    body: Dict[str, Any],
    api_key: None = Depends(verify_api_key),
) -> Dict[str, Any]:
    """Submit a task to the orchestrator.

    The request body should contain:
    * ``name``: The task name.
    * ``payload``: A dictionary of task parameters.
    """
    if not isinstance(body.get("name"), str):
        raise HTTPException(status_code=400, detail="Field 'name' must be a string")
    payload = body.get("payload", {})
    if not isinstance(payload, dict):
        raise HTTPException(status_code=400, detail="Field 'payload' must be an object")
    return orch.post_task(name=body["name"], payload=payload)