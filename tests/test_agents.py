"""Smoke tests for the Incluu agent platform."""

from incluu_agents import Orchestrator, SalesAgent, SupportAgent, AnalyticsAgent, JobsAgent, HealthAgent, LegalAgent
from fastapi.testclient import TestClient
from app.main import app


def setup_orchestrator() -> Orchestrator:
    orch = Orchestrator(log_file="/tmp/test_audit.log")
    for agent_cls in [SalesAgent, SupportAgent, AnalyticsAgent, JobsAgent, HealthAgent, LegalAgent]:
        orch.register_agent(agent_cls())
    return orch


def test_sales_agent():
    orch = setup_orchestrator()
    result = orch.post_task(name="sales_outreach", payload={"count": 2})
    assert "leads" in result
    assert len(result["leads"]) == 2


def test_jobs_agent():
    orch = setup_orchestrator()
    result = orch.post_task(name="job_search", payload={"count": 3})
    assert "jobs" in result
    assert len(result["jobs"]) == 3


def test_health_agent():
    orch = setup_orchestrator()
    result = orch.post_task(name="health_search", payload={"speciality": "Cardiologist"})
    assert "doctors" in result
    # ensure filtered doctors have speciality cardiologist
    for doc in result["doctors"]:
        assert "cardiologist" in doc["speciality"].lower()


def test_legal_agent():
    orch = setup_orchestrator()
    result = orch.post_task(name="legal_search", payload={"speciality": "Family"})
    assert "lawyers" in result
    for atty in result["lawyers"]:
        assert "family" in atty["speciality"].lower()


def test_analytics_agent():
    orch = setup_orchestrator()
    data = [1, 2, 3, 4]
    result = orch.post_task(name="generate_report", payload={"data": data})
    summary = result.get("summary")
    assert summary["mean"] == 2.5
    assert summary["min"] == 1
    assert summary["max"] == 4


def test_api_endpoints():
    client = TestClient(app)
    # health check
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json()["status"] == "ok"
    # list agents
    resp = client.get("/agents")
    assert resp.status_code == 200
    assert any(agent["name"] == "sales_agent" for agent in resp.json())
    # marketplace
    resp = client.get("/marketplace")
    assert resp.status_code == 200
    # post task
    resp = client.post("/tasks", json={"name": "sales_outreach", "payload": {"count": 1}})
    assert resp.status_code == 200
    assert "leads" in resp.json()