"""Health agent implementation."""

from __future__ import annotations

from typing import Iterable

from ..orchestrator import Agent, Task, Result, fake_doctors


class HealthAgent(Agent):
    """Agent that handles health related tasks."""

    name: str = "health_agent"
    tasks: Iterable[str] = ("health_search", "health_appointment")

    def handle(self, task: Task) -> Result:
        if task.name == "health_search":
            return Result(ok=True, data={"doctors": fake_doctors()})
        elif task.name == "health_appointment":
            doctor_id = task.payload.get("doctor_id", 1)
            date = task.payload.get("date", "2025-09-15")
            return Result(ok=True, data={"appointment": {"doctor_id": doctor_id, "date": date}})
        return Result(ok=False, error="Unknown task for HealthAgent")