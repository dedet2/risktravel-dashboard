"""JobsAgent implementation for job search and recommendations."""

from __future__ import annotations

from typing import Any, Dict

from .base import BaseAgent
from ..orchestrator import Task, Result, generate_fake_jobs


class JobsAgent(BaseAgent):
    """Agent that returns synthetic job listings for a given query."""

    name = "jobs_agent"
    tasks = ["job_search"]

    def handle_task(self, task: Task) -> Result:
        if task.name != "job_search":
            raise ValueError(f"JobsAgent cannot handle task {task.name}")
        count = int(task.payload.get("count", 5))
        jobs = generate_fake_jobs(count)
        query = task.payload.get("query")
        if query:
            query_lower = str(query).lower()
            jobs = [job for job in jobs if query_lower in job["title"].lower()]
        return self.result(jobs=jobs, message=f"Found {len(jobs)} synthetic jobs")