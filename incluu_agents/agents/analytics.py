
from ..orchestrator import Agent, Task, Result, fake_leads, fake_tickets

class AnalyticsAgent(Agent):
    name = "AnalyticsAgent"
    handles = ["analytics_report"]

    def handle(self, task: Task) -> Result:
        leads = fake_leads(10)
        tickets = fake_tickets(5)
        contacted = sum(1 for l in leads if l.get("status") == "contacted")
        return Result(ok=True, data={"contacted_leads": contacted, "total_leads": len(leads), "open_tickets": len(tickets)})
