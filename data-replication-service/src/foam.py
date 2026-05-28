import foam
from src.settings import FOAM_COLLECTOR_TOKEN, IS_PROD_ENVIRONMENT

foam.init(
    service_name="data-replication-service",
    is_production=IS_PROD_ENVIRONMENT,
    api_key=FOAM_COLLECTOR_TOKEN,
    trace_spark_jobs=True,
    trace_iceberg_operations=True,
    trace_kafka_consumers=True,
)