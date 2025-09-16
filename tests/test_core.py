"""Tests for the Incluu agent platform."""

from incluu_agents import Orchestrator, SalesAgent, SupportAgent, AnalyticsAgent, JobsAgent, HealthAgent, LegalAgent


def setup_orch() -> Orchestrator:
    orch = Orchestrator()
    for cls in [SalesAgent, SupportAgent, AnalyticsAgent, JobsAgent, HealthAgent, LegalAgent]:
        orch.register_agent(cls())
    return orch


def test_registered_agents():
    orch = setup_orch()
    names = sorted([agent.name for agent in orch.registered_agents()])
    assert names == [
        'analytics_agent',
        'health_agent',
        'jobs_agent',
        'legal_agent',
        'sales_agent',
        'support_agent',
    ]


def test_job_search():
    orch = setup_orch()
    res = orch.post_task(name='job_search', payload={'count': 2})
    assert res['ok']
    assert 'jobs' in res['data'] and len(res['data']['jobs']) == 2