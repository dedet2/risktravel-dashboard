"""Sales agent implementation."""

from __future__ import annotations

from typing import Iterable

from ..orchestrator import Agent, Task, Result, fake_leads


class SalesAgent(Agent):
    """Agent that generates sales outreach lists."""

    name: str = "sales_agent"
    tasks: Iterable[str] = ("sales_outreach", "lead_generation")

    def handle(self, task: Task) -> Result:
        # Generate leads and mark top ones as contacted
        leads = sorted(fake_leads(10), key=lambda x: x["score"], reverse=True)
        to_contact = leads[:3]
        for lead in to_contact:
            lead["status"] = "contacted"
        return Result(ok=True, data={"contacted": to_contact})