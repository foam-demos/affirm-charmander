import foam
from src.config import OTEL_FOAM_API_KEY, DEPLOYMENT_ENV

foam.init(
    service_name="ml-feature-platform",
    is_production=(DEPLOYMENT_ENV == "production"),
    api_key=OTEL_FOAM_API_KEY,
    trace_redis=True,
    trace_db_queries=True,
    performance_monitoring=True,
)