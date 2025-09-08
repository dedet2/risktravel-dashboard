"""LegalAgent implementation for legal research and appointments."""

from __future__ import annotations

from typing import Any, Dict

from .base import BaseAgent
from ..orchestrator import Task, Result, generate_fake_lawyers


class LegalAgent(BaseAgent):
    """Agent that handles legal searches and appointment scheduling."""

    name = "legal_agent"
    tasks = ["legal_search", "legal_appointment"]

    def handle_task(self, task: Task) -> Result:
        if task.name == "legal_search":
            speciality = task.payload.get("speciality")
            lawyers = generate_fake_lawyers(5)
            if speciality:
                speciality_lower = speciality.lower()
                lawyers = [l for l in lawyers if speciality_lower in l["speciality"].lower()]
            return self.result(lawyers=lawyers, message=f"Found {len(lawyers)} lawyers")
        elif task.name == "legal_appointment":
            lawyer_name = task.payload.get("lawyer_name")
            date = task.payload.get("date")
            return self.result(confirmation=f"Appointment booked with {lawyer_name} on {date}")
        else:
            raise ValueError(f"LegalAgent cannot handle task {task.name}")