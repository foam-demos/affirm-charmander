import foam
from src.config import FOAM_API_KEY, IS_PRODUCTION

foam.init(
    service_name="loan-decisioning-api",
    is_production=IS_PRODUCTION,
    api_key=FOAM_API_KEY,
    auto_instrument=True,
    trace_db_queries=True,
    trace_http_clients=True,
)