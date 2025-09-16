"""Legal agent implementation."""

from __future__ import annotations

from typing import Iterable

from ..orchestrator import Agent, Task, Result, fake_lawyers


class LegalAgent(Agent):
    """Agent that handles legal related tasks."""

    name: str = "legal_agent"
    tasks: Iterable[str] = ("legal_search", "legal_appointment")

    def handle(self, task: Task) -> Result:
        if task.name == "legal_search":
            return Result(ok=True, data={"lawyers": fake_lawyers()})
        elif task.name == "legal_appointment":
            lawyer_id = task.payload.get("lawyer_id", 1)
            date = task.payload.get("date", "2025-09-20")
            return Result(ok=True, data={"appointment": {"lawyer_id": lawyer_id, "date": date}})
        return Result(ok=False, error="Unknown task for LegalAgent")