
# Incluu Agent Service (RiskTravel Dashboard)
Minimal, production-leaning agent service you can run locally or deploy.

## Quickstart (copy–paste)
1. Install Python 3.11+
2. Clone your repo and copy this folder's contents into the root.
3. In a terminal from the project root:
   ```bash
   pip install -r requirements.txt
   make test
   make run
   ```
4. Open http://localhost:8000/docs to try the API:
   - `GET /agents`
   - `POST /tasks` with body:
     ```json
     {"name": "sales_outreach", "payload": {"count": 3}}
     ```

## Files
- `incluu_agents/` – orchestrator + agents
- `app/main.py` – FastAPI app
- `tests/` – pytest
- `requirements.txt`, `Dockerfile`, `.env.example`, `Makefile`

## Next
- Add CRM/helpdesk connectors.
- Add auth (API keys/JWT) and request logging.
- Extend agents for life‑management (jobs, health, legal) as discussed.
