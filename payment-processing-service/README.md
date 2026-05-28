# Payment Processing Service

Core payment orchestration service handling transaction processing, money movement, virtual card issuance, and reconciliation with banking partners. Handles critical financial workloads with zero tolerance for errors.

**Stack**: Python 3.11, FastAPI, asyncpg (Aurora PostgreSQL), SQLAlchemy, Celery

**Run**: `docker-compose up db redis` then `python src/main.py`