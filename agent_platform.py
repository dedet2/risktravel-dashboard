"""
Minimal AI‑agent platform prototype for synthetic testing.

This module defines a simple orchestration framework and a few example agents.
It is designed for demonstration and rapid prototyping purposes and is not
production ready.  Security hooks and authentication are stubbed for
expansion in future iterations.

Usage:
    from agent_platform import Orchestrator, SalesAgent, SupportAgent, AnalyticsAgent

    orchestrator = Orchestrator()
    orchestrator.register_agent(SalesAgent())
    orchestrator.register_agent(SupportAgent())
    orchestrator.register_agent(AnalyticsAgent())

    # Post tasks to orchestrator
    orchestrator.post_task({"type": "sales_outreach", "count": 3})
    orchestrator.post_task({"type": "support_summary"})
    orchestrator.post_task({"type": "analytics_report"})

    # Run the event loop once
    orchestrator.run_once()

"""

import random
import string
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


def stub_authenticate(token: Optional[str]) -> bool:
    """Stubbed authentication check.  Returns True if token is provided.

    In a real system this would validate a JWT or session token against
    an identity provider.
    """
    return token is not None


def stub_authorise(user: str, action: str) -> bool:
    """Stubbed authorisation check.  Always returns True for this prototype.

    A production implementation would consult an RBAC/ABAC policy.
    """
    return True


@dataclass
class Task:
    """Represents a unit of work for an agent to perform."""
    type: str
    payload: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Result:
    """Represents the result produced by an agent."""
    task_type: str
    data: Any


class Agent:
    """Base class for all agents.  Subclasses must implement execute()."""

    name: str = "base"

    def execute(self, task: Task) -> Optional[Result]:
        raise NotImplementedError

    def describe(self) -> str:
        return f"Agent {self.name}"


class SalesAgent(Agent):
    """A simple agent that generates and prioritises synthetic leads."""

    name = "SalesAgent"

    def __init__(self):
        # Prepopulate with some synthetic leads
        self.leads = self._generate_leads(10)

    def _generate_leads(self, n: int) -> List[Dict[str, Any]]:
        industries = ["SaaS", "Retail", "Healthcare", "Finance"]
        return [
            {
                "id": i,
                "name": self._random_name(),
                "industry": random.choice(industries),
                "email": f"lead{i}@example.com",
                "score": random.randint(1, 100),
            }
            for i in range(n)
        ]

    def _random_name(self) -> str:
        first = ''.join(random.choices(string.ascii_uppercase, k=5))
        last = ''.join(random.choices(string.ascii_uppercase, k=7))
        return f"{first} {last}"

    def execute(self, task: Task) -> Optional[Result]:
        if task.type == "sales_outreach":
            count = task.payload.get("count", 1)
            # Sort leads by descending score and pick top N
            leads_sorted = sorted(self.leads, key=lambda x: x["score"], reverse=True)
            selected = leads_sorted[:count]
            # Simulate sending outreach emails
            for lead in selected:
                lead["status"] = "contacted"
            return Result(task_type=task.type, data={"contacted_leads": selected})
        return None


class SupportAgent(Agent):
    """An agent that summarises support tickets and suggests responses."""

    name = "SupportAgent"

    def __init__(self):
        self.tickets = self._generate_tickets(5)

    def _generate_tickets(self, n: int) -> List[Dict[str, Any]]:
        categories = ["billing", "technical", "product", "other"]
        descriptions = [
            "Cannot login to account",
            "Payment failed",
            "Bug in latest update",
            "Feature request"
        ]
        return [
            {
                "id": i,
                "category": random.choice(categories),
                "description": random.choice(descriptions),
                "customer": f"customer{i}@example.com",
                "status": "open",
            }
            for i in range(n)
        ]

    def execute(self, task: Task) -> Optional[Result]:
        if task.type == "support_summary":
            # Count tickets by category
            summary: Dict[str, int] = {}
            for ticket in self.tickets:
                summary[ticket["category"]] = summary.get(ticket["category"], 0) + 1
            # Suggest responses for open tickets
            suggestions = [
                {
                    "id": ticket["id"],
                    "response": f"Hello, regarding your issue '{ticket['description']}', our team is investigating."
                }
                for ticket in self.tickets if ticket["status"] == "open"
            ]
            return Result(task_type=task.type, data={"summary": summary, "suggestions": suggestions})
        return None


class AnalyticsAgent(Agent):
    """Aggregates metrics from other agents and produces simple reports."""

    name = "AnalyticsAgent"

    def __init__(self, sales_agent: SalesAgent, support_agent: SupportAgent):
        self.sales_agent = sales_agent
        self.support_agent = support_agent

    def execute(self, task: Task) -> Optional[Result]:
        if task.type == "analytics_report":
            # Count contacted leads
            contacted = [lead for lead in self.sales_agent.leads if lead.get("status") == "contacted"]
            ticket_count = len(self.support_agent.tickets)
            return Result(
                task_type=task.type,
                data={
                    "contacted_leads": len(contacted),
                    "total_leads": len(self.sales_agent.leads),
                    "open_tickets": ticket_count,
                },
            )
        return None


class Orchestrator:
    """Coordinates tasks between agents using a simple event queue."""

    def __init__(self):
        self.agents: List[Agent] = []
        self.task_queue: List[Task] = []

    def register_agent(self, agent: Agent) -> None:
        print(f"Registering {agent.describe()}")
        self.agents.append(agent)

    def post_task(self, task_payload: Dict[str, Any]) -> None:
        """Add a task to the queue.  task_payload must include 'type'."""
        task_type = task_payload.get("type")
        if not task_type:
            raise ValueError("Task payload must include a 'type'")
        task = Task(type=task_type, payload={k: v for k, v in task_payload.items() if k != "type"})
        print(f"Posting task: {task.type} with payload {task.payload}")
        self.task_queue.append(task)

    def run_once(self) -> None:
        """Process all tasks currently in the queue once."""
        while self.task_queue:
            task = self.task_queue.pop(0)
            handled = False
            for agent in self.agents:
                result = agent.execute(task)
                if result is not None:
                    handled = True
                    print(f"Task '{task.type}' handled by {agent.name}: {result.data}")
                    break
            if not handled:
                print(f"No agent could handle task '{task.type}'")


def demo():
    """Run a simple demonstration of the orchestrator with synthetic data."""
    # Instantiate agents
    sales_agent = SalesAgent()
    support_agent = SupportAgent()
    analytics_agent = AnalyticsAgent(sales_agent, support_agent)

    orchestrator = Orchestrator()
    orchestrator.register_agent(sales_agent)
    orchestrator.register_agent(support_agent)
    orchestrator.register_agent(analytics_agent)

    # Post example tasks
    orchestrator.post_task({"type": "sales_outreach", "count": 3})
    orchestrator.post_task({"type": "support_summary"})
    orchestrator.post_task({"type": "analytics_report"})

    # Process tasks
    orchestrator.run_once()


if __name__ == "__main__":
    demo()