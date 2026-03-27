from airflow.models import BaseOperator

class JobProcessOperator(BaseOperator):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def execute(self, context):
        records = context['ti'].xcom_pull(
            task_ids='fetch_task',
            key='records'
        )

        if not records:
            print("No records found to process.")
            return

        print(f"Processing records: {records}")

        # Assuming record has an id as first element
        max_id = max(record[0] for record in records)
        
        context['ti'].xcom_push(key='last_id', value=max_id)
        
        print(f"Pushed max_id ({max_id}) to XCom.")
        return max_id