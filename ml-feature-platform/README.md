# ML Feature Platform

Self-serve platform for developing and serving ML features for real-time decisioning. Manages feature computation, online/offline storage, and low-latency serving with Redis caching and MySQL fallback.

**Stack**: Python 3.11, FastAPI, Redis, asyncpg, Apache Spark

**Local dev**: `docker-compose up` • **Feature computation**: `spark-submit src/jobs/compute_features.py`