"""Analytics agent implementation."""

from __future__ import annotations

from typing import Iterable

from ..orchestrator import Agent, Task, Result, fake_leads, fake_tickets


class AnalyticsAgent(Agent):
    """Agent that generates simple KPI reports."""

    name: str = "analytics_agent"
    tasks: Iterable[str] = ("generate_report",)

    def handle(self, task: Task) -> Result:
        leads = fake_leads(10)
        tickets = fake_tickets(6)
        kpis = {
            "total_leads": len(leads),
            "avg_lead_score": sum(l["score"] for l in leads) / len(leads),
            "open_tickets": len(tickets),
        }
        return Result(ok=True, data={"kpis": kpis})