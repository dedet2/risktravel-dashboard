"""AnalyticsAgent implementation for summarising numeric datasets."""

from __future__ import annotations

from typing import Any, Dict, List
import statistics

from .base import BaseAgent
from ..orchestrator import Task, Result


class AnalyticsAgent(BaseAgent):
    """Agent that performs simple analytics on numeric lists."""

    name = "analytics_agent"
    tasks = ["generate_report"]

    def handle_task(self, task: Task) -> Result:
        if task.name != "generate_report":
            raise ValueError(f"AnalyticsAgent cannot handle task {task.name}")
        data = task.payload.get("data")
        if not isinstance(data, list) or not data:
            return self.result(message="No data provided", summary={})
        numbers = [float(x) for x in data]
        summary = {
            "count": len(numbers),
            "mean": statistics.mean(numbers),
            "median": statistics.median(numbers),
            "min": min(numbers),
            "max": max(numbers),
        }
        return self.result(summary=summary)