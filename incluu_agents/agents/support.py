
from collections import Counter
from ..orchestrator import Agent, Task, Result, fake_tickets

class SupportAgent(Agent):
    name = "SupportAgent"
    handles = ["support_summary"]

    def handle(self, task: Task) -> Result:
        tickets = fake_tickets(5)
        summary = Counter(t["issue"].split()[0].lower() for t in tickets)
        suggestions = [{"id": t["id"], "response": f"Thanks—re: '{t['issue']}', we're investigating."} for t in tickets]
        return Result(ok=True, data={"summary": dict(summary), "suggestions": suggestions})
