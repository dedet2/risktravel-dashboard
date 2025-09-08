
from typing import Dict, Any, Callable, List
import random
from dataclasses import dataclass, field

@dataclass
class Task:
    name: str
    payload: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Result:
    ok: bool
    data: Dict[str, Any] = field(default_factory=dict)
    error: str = ""

class Agent:
    name: str = "base"
    handles: List[str] = []

    def handle(self, task: Task) -> Result:
        return Result(ok=False, error="Not implemented")

class Orchestrator:
    def __init__(self):
        self._registry: Dict[str, Agent] = {}
        self._routes: Dict[str, str] = {}

    def register(self, agent: Agent):
        self._registry[agent.name] = agent
        for t in agent.handles:
            self._routes[t] = agent.name

    def submit(self, task: Task) -> Result:
        agent_name = self._routes.get(task.name)
        if not agent_name:
            return Result(ok=False, error=f"No agent for task '{task.name}'")
        agent = self._registry[agent_name]
        try:
            return agent.handle(task)
        except Exception as e:
            return Result(ok=False, error=str(e))

# Synthetic data helpers
FIRST = ["Ava","Kai","Maya","Liam","Zoe","Noah","Ivy","Leo","Mia","Eli"]
LAST  = ["Stone","Rivera","Chen","Walker","Singh","Lopez","Kim","Ali","King","Patel"]
INDUSTRIES = ["SaaS","Finance","Retail","Health","Media"]
ISSUES = ["Cannot login","Payment failed","Bug in latest update","Feature request","Account locked"]

def fake_leads(n=10):
    out = []
    for i in range(n):
        out.append({
            "id": i+1,
            "name": f"{random.choice(FIRST)} {random.choice(LAST)}",
            "industry": random.choice(INDUSTRIES),
            "email": f"lead{i+1}@example.com",
            "score": random.randint(60, 98),
            "status": "new"
        })
    return out

def fake_tickets(n=5):
    return [{"id": i, "issue": random.choice(ISSUES)} for i in range(n)]
