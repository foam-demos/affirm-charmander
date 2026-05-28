import foam
from src.settings import FOAM_BEARER_TOKEN, IS_PRODUCTION_MODE

foam.init(
    service_name="payment-processing-service",
    is_production=IS_PRODUCTION_MODE,
    api_key=f"Bearer {FOAM_BEARER_TOKEN}",
    trace_db_queries=True,
    trace_celery_tasks=True,
    trace_external_apis=True,
)