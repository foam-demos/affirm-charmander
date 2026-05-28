# Loan Decisioning API

Real-time credit decisioning service that evaluates consumer loan applications using ML models and alternative credit data. Built with Python/FastAPI, integrates with ML Feature Platform and Training & Serving Platform for sub-3-second approval decisions.

**Stack**: Python 3.11, FastAPI, asyncpg, aiohttp, Redis

**Run locally**: `docker-compose up` then `uvicorn src.main:app --reload`