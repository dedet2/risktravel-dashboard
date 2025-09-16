"""Jobs agent implementation."""

from __future__ import annotations

from typing import Iterable

from ..orchestrator import Agent, Task, Result, fake_jobs


class JobsAgent(Agent):
    """Agent that returns synthetic job listings."""

    name: str = "jobs_agent"
    tasks: Iterable[str] = ("job_search",)

    def handle(self, task: Task) -> Result:
        count = int(task.payload.get("count", 3))
        jobs = fake_jobs(count)
        return Result(ok=True, data={"jobs": jobs})