"""Quick local self‑check script.

This script initialises the orchestrator, registers all agents and
executes a sample job search task. It prints results to stdout and
exits. This allows verifying basic functionality without pytest.
"""

from incluu_agents import Orchestrator, SalesAgent, SupportAgent, AnalyticsAgent, JobsAgent, HealthAgent, LegalAgent

def main():
    orch = Orchestrator()
    for cls in [SalesAgent, SupportAgent, AnalyticsAgent, JobsAgent, HealthAgent, LegalAgent]:
        orch.register_agent(cls())
    print("Registered agents:", [agent.name for agent in orch.registered_agents()])
    result = orch.post_task(name='job_search', payload={'count': 2})
    print("Job search result:", result)
    print("OK ✅")

if __name__ == '__main__':
    main()