from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

# Import the custom operator we created
from operators.sample_operator import SampleOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def print_result(ti):
    """
    Print the result retrieved from the SampleOperator via XCom.
    """
    result = ti.xcom_pull(task_ids='use_my_custom_operator')
    print(f"Result fetched from custom operator: {result}")

with DAG(
    'sample_plugin_dag',
    default_args=default_args,
    description='A simple tutorial DAG using a custom hook and operator',
    schedule=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['example', 'custom-plugin'],
) as dag:

    # 1. Use the custom operator here
    run_custom_operator = SampleOperator(
        task_id='use_my_custom_operator',
        sample_conn_id='my_test_connection',
        endpoint='/api/v1/dummy_data'
    )

    # 2. Use a Python operator to read the result using XCom
    print_task = PythonOperator(
        task_id='print_task',
        python_callable=print_result
    )

    # Define the dependency
    run_custom_operator >> print_task
