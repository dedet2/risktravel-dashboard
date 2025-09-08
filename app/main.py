
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict, Any
from incluu_agents.orchestrator import Orchestrator, Task
from incluu_agents.agents.sales import SalesAgent
from incluu_agents.agents.support import SupportAgent
from incluu_agents.agents.analytics import AnalyticsAgent

app = FastAPI(title="Incluu Agent Service", version="0.1.0")
orch = Orchestrator()
for a in (SalesAgent(), SupportAgent(), AnalyticsAgent()):
    orch.register(a)

class TaskIn(BaseModel):
    name: str
    payload: Dict[str, Any] = {}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/agents")
def agents():
    return {"agents": list(orch._registry.keys())}

@app.post("/tasks")
def submit(task: TaskIn):
    res = orch.submit(Task(name=task.name, payload=task.payload))
    return {"ok": res.ok, "data": res.data, "error": res.error}
