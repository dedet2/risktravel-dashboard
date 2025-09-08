"""Base definitions for all agent implementations."""

from __future__ import annotations

from typing import Dict, Any, List
from ..orchestrator import Task, Result, Agent


class BaseAgent(Agent):
    """Convenience base class for concrete agent implementations.

    Deriving from this class provides access to the :class:`Task`
    definition and a helper ``result`` method for constructing
    ``Result`` instances. Subclasses should override the ``tasks``
    attribute and implement the ``handle_task`` method.
    """

    name: str = "base"
    tasks: List[str] = []

    def result(self, **kwargs: Any) -> Result:
        """Construct a result dictionary."""
        return Result(**kwargs)