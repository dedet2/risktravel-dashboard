"""SalesAgent implementation for generating synthetic sales outreach."""

from __future__ import annotations

from typing import Any, Dict

from .base import BaseAgent
from ..orchestrator import generate_fake_leads, Task, Result


class SalesAgent(BaseAgent):
    """Agent responsible for generating outreach lists and emails."""

    name = "sales_agent"
    tasks = ["sales_outreach", "lead_generation"]

    def handle_task(self, task: Task) -> Result:
        if task.name == "sales_outreach":
            count = int(task.payload.get("count", 5))
            leads = generate_fake_leads(count)
            return self.result(leads=leads, message=f"Generated {len(leads)} synthetic leads")
        elif task.name == "lead_generation":
            # alias to sales_outreach
            return self.handle_task(Task(name="sales_outreach", payload=task.payload))
        else:
            raise ValueError(f"SalesAgent cannot handle task {task.name}")