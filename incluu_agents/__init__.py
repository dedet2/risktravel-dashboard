"""Top‑level package for Incluu Agents.

This module exposes the :class:`Orchestrator` class and all available agent
types. It allows consumers to import a single namespace instead of
referencing individual modules.

The orchestrator implements a simple message bus that brokers tasks
between registered agents. Each agent advertises the task names it can
handle via a ``tasks`` attribute. When a task is posted the orchestrator
will route the task to the appropriate agent and return the result.

Example::

    from incluu_agents import Orchestrator, SalesAgent, SupportAgent

    orch = Orchestrator()
    orch.register_agent(SalesAgent())
    orch.register_agent(SupportAgent())
    result = orch.post_task(name="sales_outreach", payload={"count": 10})
    print(result)

"""

from .orchestrator import Orchestrator, Task, Result  # noqa: F401
from .agents.sales import SalesAgent  # noqa: F401
from .agents.support import SupportAgent  # noqa: F401
from .agents.analytics import AnalyticsAgent  # noqa: F401
from .agents.jobs import JobsAgent  # noqa: F401
from .agents.health import HealthAgent  # noqa: F401
from .agents.legal import LegalAgent  # noqa: F401