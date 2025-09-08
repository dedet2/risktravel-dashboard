
from incluu_agents.orchestrator import Orchestrator, Task
from incluu_agents.agents.sales import SalesAgent
from incluu_agents.agents.support import SupportAgent
from incluu_agents.agents.analytics import AnalyticsAgent

def test_end_to_end():
    orch = Orchestrator()
    for a in (SalesAgent(), SupportAgent(), AnalyticsAgent()):
        orch.register(a)
    r1 = orch.submit(Task(name="sales_outreach", payload={"count": 2}))
    r2 = orch.submit(Task(name="support_summary"))
    r3 = orch.submit(Task(name="analytics_report"))
    assert r1.ok and r2.ok and r3.ok
    assert len(r1.data["contacted_leads"]) == 2
