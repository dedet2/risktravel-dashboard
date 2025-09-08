"""Core orchestrator for routing tasks to AI agents.

The :class:`Orchestrator` maintains a registry of agents. Each agent
advertises which tasks it can handle via its ``tasks`` attribute. When
a task is posted the orchestrator looks up the registered agents and
delegates execution. If multiple agents can handle a task the first
registered agent is used.

An audit log is written for every task processed. The log records the
timestamp, agent name, task name, input payload and result. This log
can be used for compliance and debugging. The log file location is
configurable via the ``log_file`` constructor argument.

The orchestrator is deliberately lightweight. More advanced features
such as concurrent task processing, retries and scheduling can be added
over time.
"""

from __future__ import annotations

import json
import logging
import os
import random
from datetime import datetime
from typing import Any, Dict, Iterable, List, Optional


class Task:
    """Represents a unit of work to be handled by an agent.

    Args:
        name: A string identifying the task (e.g. ``"sales_outreach"``).
        payload: Arbitrary data associated with the task. Must be JSON
            serialisable.

    The orchestrator does not interpret the payload; it simply passes
    it to the agent responsible for the task.
    """

    def __init__(self, name: str, payload: Dict[str, Any]):
        self.name = name
        self.payload = payload


class Result(Dict[str, Any]):
    """A dictionary subclass representing the result of a task."""

    def __str__(self) -> str:
        return json.dumps(self, indent=2)


class Agent:
    """Base class for all agents.

    Subclasses must define a ``name`` attribute and a ``tasks`` list of
    task names they can handle. They must also implement a
    ``handle_task`` method that accepts a :class:`Task` and returns a
    :class:`Result`.
    """

    name: str = "agent"
    tasks: List[str] = []

    def handle_task(self, task: Task) -> Result:
        raise NotImplementedError


class Orchestrator:
    """Simple orchestrator to route tasks to registered agents."""

    def __init__(self, log_file: Optional[str] = None) -> None:
        self._agents: List[Agent] = []
        self.log_file = log_file or os.environ.get("AGENT_AUDIT_LOG", "agent_audit.log")
        # Configure logging
        self.logger = logging.getLogger("Orchestrator")
        self.logger.setLevel(logging.INFO)
        # Avoid adding multiple handlers if multiple orchestrators are created
        if not self.logger.handlers:
            handler = logging.FileHandler(self.log_file)
            formatter = logging.Formatter("%(asctime)s - %(message)s")
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def register_agent(self, agent: Agent) -> None:
        """Register an agent so that it can receive tasks.

        Args:
            agent: An instance of a subclass of :class:`Agent`.
        """
        self._agents.append(agent)

    def registered_agents(self) -> Iterable[Agent]:
        """Return an iterable of all registered agents."""
        return list(self._agents)

    def post_task(self, name: str, payload: Dict[str, Any]) -> Result:
        """Post a task to the orchestrator and return the result.

        Args:
            name: The task name.
            payload: The payload for the task.

        Returns:
            A :class:`Result` returned by the handling agent.

        Raises:
            ValueError: If no agent can handle the task name.
        """
        task = Task(name=name, payload=payload)
        for agent in self._agents:
            if name in getattr(agent, "tasks", []):
                result = agent.handle_task(task)
                # Audit log
                self._audit(task, agent, result)
                return result
        raise ValueError(f"No agent registered to handle task '{name}'")

    def _audit(self, task: Task, agent: Agent, result: Result) -> None:
        """Write an audit entry to the log file."""
        entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "agent": agent.name,
            "task": task.name,
            "payload": task.payload,
            "result": result,
        }
        self.logger.info(json.dumps(entry))


def generate_fake_leads(count: int = 5) -> List[Dict[str, Any]]:
    """Generate a list of synthetic sales leads."""
    companies = ["Acme Corp", "Globex", "Initech", "Umbrella", "Soylent"]
    first_names = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"]
    last_names = ["Smith", "Johnson", "Lee", "Brown", "Davis"]
    leads = []
    for _ in range(count):
        name = f"{random.choice(first_names)} {random.choice(last_names)}"
        leads.append({
            "name": name,
            "company": random.choice(companies),
            "email": f"{name.lower().replace(' ', '.')}@example.com",
            "phone": f"555-{random.randint(100,999)}-{random.randint(1000,9999)}",
        })
    return leads


def generate_fake_jobs(count: int = 5) -> List[Dict[str, Any]]:
    """Generate a list of synthetic job openings."""
    titles = ["Software Engineer", "Data Analyst", "Project Manager", "Product Designer"]
    companies = ["Techify", "DataCorp", "InnovateX", "FutureWorks"]
    jobs = []
    for _ in range(count):
        title = random.choice(titles)
        company = random.choice(companies)
        jobs.append({
            "title": title,
            "company": company,
            "location": random.choice(["Remote", "San Francisco", "New York", "Austin"]),
            "salary_range": f"${random.randint(80,150)}k-${random.randint(150,250)}k",
            "description": f"We are seeking a {title} to join our {company} team.",
        })
    return jobs


def generate_fake_doctors(count: int = 5) -> List[Dict[str, Any]]:
    """Generate a list of synthetic doctors."""
    specialities = ["General Practitioner", "Cardiologist", "Dermatologist", "Neurologist"]
    names = ["Dr. Chen", "Dr. Patel", "Dr. Garcia", "Dr. Nguyen"]
    doctors = []
    for _ in range(count):
        doctors.append({
            "name": random.choice(names),
            "speciality": random.choice(specialities),
            "location": random.choice(["Oakland", "San Jose", "San Francisco", "Berkeley"]),
            "next_available": f"2025-09-{random.randint(10,30)}",
        })
    return doctors


def generate_fake_lawyers(count: int = 5) -> List[Dict[str, Any]]:
    """Generate a list of synthetic lawyers."""
    specialities = ["Corporate", "Family", "Criminal", "Immigration"]
    names = ["Atty. Kim", "Atty. Johnson", "Atty. Singh", "Atty. Martinez"]
    lawyers = []
    for _ in range(count):
        lawyers.append({
            "name": random.choice(names),
            "speciality": random.choice(specialities),
            "location": random.choice(["Oakland", "San Jose", "San Francisco", "Berkeley"]),
            "next_available": f"2025-09-{random.randint(10,30)}",
        })
    return lawyers