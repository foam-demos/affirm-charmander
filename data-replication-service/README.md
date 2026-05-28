# Data Replication Service

CDC-based replication pipeline streaming MySQL operational data to Apache Iceberg data lake on S3. Handles thousands of tables with time-travel requirements and UTC0 snapshot validation for regulatory financial reporting.

**Stack**: Python 3.11, Apache Spark, Apache Iceberg, Debezium CDC, Kafka

**Run**: `spark-submit --packages org.apache.iceberg:iceberg-spark-runtime-3.3_2.12:1.3.0 src/replicate.py`