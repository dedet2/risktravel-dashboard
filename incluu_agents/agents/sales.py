
from ..orchestrator import Agent, Task, Result, fake_leads
import random

class SalesAgent(Agent):
    name = "SalesAgent"
    handles = ["sales_outreach"]

    def handle(self, task: Task) -> Result:
        count = int(task.payload.get("count", 3))
        leads = sorted(fake_leads(10), key=lambda x: x["score"], reverse=True)[:count]
        for l in leads:
            l["status"] = "contacted"
        return Result(ok=True, data={"contacted_leads": leads})
