"""HealthAgent implementation for health‑related queries and appointments."""

from __future__ import annotations

from typing import Any, Dict

from .base import BaseAgent
from ..orchestrator import Task, Result, generate_fake_doctors


class HealthAgent(BaseAgent):
    """Agent that handles health searches and appointment scheduling."""

    name = "health_agent"
    tasks = ["health_search", "health_appointment"]

    def handle_task(self, task: Task) -> Result:
        if task.name == "health_search":
            speciality = task.payload.get("speciality")
            doctors = generate_fake_doctors(5)
            if speciality:
                speciality_lower = speciality.lower()
                doctors = [d for d in doctors if speciality_lower in d["speciality"].lower()]
            return self.result(doctors=doctors, message=f"Found {len(doctors)} doctors")
        elif task.name == "health_appointment":
            doctor_name = task.payload.get("doctor_name")
            date = task.payload.get("date")
            # In a real system we would verify the doctor and time availability
            return self.result(confirmation=f"Appointment booked with {doctor_name} on {date}")
        else:
            raise ValueError(f"HealthAgent cannot handle task {task.name}")