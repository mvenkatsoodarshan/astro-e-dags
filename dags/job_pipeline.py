from airflow import DAG
from datetime import datetime
from plugins.operators.job_operator import JobFetchOperator
from plugins.operators.job_process_operator import JobProcessOperator

with DAG(
    dag_id="job_pipeline",
    start_date=datetime(2024,1,1),
    schedule="@daily",
    catchup=False
) as dag:

    fetch_task = JobFetchOperator(
        task_id="fetch_task"
    )

    process_task = JobProcessOperator(
        task_id="process_task"
    )

    fetch_task >> process_task