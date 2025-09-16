"""Support agent implementation."""

from __future__ import annotations

from collections import Counter
from typing import Iterable

from ..orchestrator import Agent, Task, Result, fake_tickets


class SupportAgent(Agent):
    """Agent that provides support ticket summaries and responses."""

    name: str = "support_agent"
    tasks: Iterable[str] = ("support_summary", "customer_support")

    def handle(self, task: Task) -> Result:
        tickets = fake_tickets(6)
        # Summarise issues by first word
        summary = Counter(ticket["issue"].split()[0].lower() for ticket in tickets)
        suggestions = [
            {"id": ticket["id"], "response": f"We are looking into: {ticket['issue']}"}
            for ticket in tickets
        ]
        return Result(ok=True, data={"summary": dict(summary), "suggestions": suggestions})