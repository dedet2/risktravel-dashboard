"""Core orchestrator and synthetic data helpers.

This module defines a simple orchestrator class that routes tasks
between registered agents. Each agent advertises the task names it
supports. The orchestrator logs tasks to a file and returns
structured results from agents.
"""

from __future__ import annotations

import json
import logging
import os
import random
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, Iterable, List, Optional

logging.basicConfig(
    filename=os.environ.get("AGENT_AUDIT_LOG", "agent_audit.log"),
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

@dataclass
class Task:
    """Represents a unit of work to be handled by an agent."""
    name: str
    payload: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Result:
    """Represents the result of a task."""
    ok: bool
    data: Dict[str, Any] = field(default_factory=dict)
    error: Optional[str] = None


class Agent:
    """Base class for all agents.

    Subclasses should define a unique ``name`` and a list of
    ``tasks`` they can handle. They must implement ``handle`` to
    process a :class:`Task` and return a :class:`Result`.
    """
    name: str = "agent"
    tasks: Iterable[str] = ()

    def handle(self, task: Task) -> Result:
        raise NotImplementedError


class Orchestrator:
    """Registers agents and routes tasks to them."""

    def __init__(self) -> None:
        self._agents: Dict[str, Agent] = {}
        self._routes: Dict[str, str] = {}

    def register_agent(self, agent: Agent) -> None:
        """Register an agent and map its tasks."""
        if agent.name in self._agents:
            raise ValueError(f"Agent name '{agent.name}' already registered")
        self._agents[agent.name] = agent
        for task_name in agent.tasks:
            self._routes[task_name] = agent.name

    def registered_agents(self) -> List[Agent]:
        """Return a list of registered agents."""
        return list(self._agents.values())

    def post_task(self, name: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """Route a task to the appropriate agent and return its result."""
        logging.info(json.dumps({"task": name, "payload": payload}))
        agent_name = self._routes.get(name)
        if not agent_name:
            return {"ok": False, "data": {}, "error": f"No agent for task '{name}'"}
        agent = self._agents[agent_name]
        try:
            result: Result = agent.handle(Task(name=name, payload=payload))
            logging.info(json.dumps({"agent": agent_name, "ok": result.ok}))
            return {
                "ok": result.ok,
                "data": result.data,
                "error": result.error,
            }
        except Exception as exc:
            logging.exception("Agent execution error")
            return {"ok": False, "data": {}, "error": str(exc)}


# Synthetic data helpers

_FIRST_NAMES = ["Ava", "Kai", "Maya", "Liam", "Zoe", "Noah", "Ivy", "Leo", "Mia", "Eli"]
_LAST_NAMES = ["Stone", "Rivera", "Chen", "Walker", "Singh", "Lopez", "Kim", "Ali", "King", "Patel"]
_JOB_TITLES = ["Software Engineer", "Product Manager", "Data Analyst", "Sales Manager"]
_DOCTORS = ["Dr. Kim - Family", "Dr. Chen - Cardiology", "Dr. Patel - Dermatology"]
_LAWYERS = ["Atty. Rivera - Corporate", "Atty. Singh - Immigration", "Atty. Lopez - Real Estate"]


def fake_leads(n: int = 10) -> List[Dict[str, Any]]:
    """Generate synthetic sales leads."""
    leads = []
    for i in range(n):
        name = f"{random.choice(_FIRST_NAMES)} {random.choice(_LAST_NAMES)}"
        leads.append({
            "id": i + 1,
            "name": name,
            "email": f"{name.lower().replace(' ', '.')}@example.com",
            "score": random.randint(60, 99),
            "status": "new",
        })
    return leads


def fake_jobs(n: int = 5) -> List[Dict[str, Any]]:
    """Generate synthetic job listings."""
    jobs = []
    for i in range(n):
        jobs.append({
            "id": i + 1,
            "title": random.choice(_JOB_TITLES),
            "company": f"Company{i + 1}",
            "location": random.choice(["Remote", "New York", "San Francisco", "Austin"]),
        })
    return jobs


def fake_doctors() -> List[Dict[str, Any]]:
    """Return a list of synthetic doctors."""
    return [
        {"id": i + 1, "name": doc, "location": "City Clinic"}
        for i, doc in enumerate(_DOCTORS)
    ]


def fake_lawyers() -> List[Dict[str, Any]]:
    """Return a list of synthetic lawyers."""
    return [
        {"id": i + 1, "name": lawyer, "location": "Downtown Office"}
        for i, lawyer in enumerate(_LAWYERS)
    ]


def fake_tickets(n: int = 5) -> List[Dict[str, Any]]:
    """Generate synthetic support tickets."""
    issues = ["Cannot login", "Payment failed", "Bug in latest update", "Feature request", "Account locked"]
    return [{"id": i + 1, "issue": random.choice(issues)} for i in range(n)]