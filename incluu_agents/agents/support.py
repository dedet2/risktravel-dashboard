"""SupportAgent implementation for handling customer support queries."""

from __future__ import annotations

from typing import Any, Dict

from .base import BaseAgent
from ..orchestrator import Task, Result


class SupportAgent(BaseAgent):
    """Agent that replies to simple support queries with canned responses."""

    name = "support_agent"
    tasks = ["support_query", "customer_support"]

    RESPONSES = {
        "refund": "We're sorry to hear that. Your refund has been processed.",
        "pricing": "Our pricing plans start at $49 per month.",
        "bug": "Thank you for reporting this bug. We've escalated it to our engineers.",
    }

    def handle_task(self, task: Task) -> Result:
        question: str = task.payload.get("query", "").lower()
        for keyword, response in self.RESPONSES.items():
            if keyword in question:
                return self.result(response=response)
        # Default fallback
        return self.result(response="Thank you for reaching out. We'll get back to you soon.")