from airflow.models import BaseOperator
from plugins.hooks.job_hook import JobHook

class JobFetchOperator(BaseOperator):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def execute(self, context):
        hook = JobHook()

        # Get last processed id from XCom
        last_id = context['ti'].xcom_pull(
            task_ids='process_task',
            key='last_id',
            include_prior_dates=True
        )

        if not last_id:
            last_id = 0

        records = hook.get_new_records(last_id)

        print(f"Fetched records: {records}")

        # Push records to next task
        context['ti'].xcom_push(key='records', value=records)

        return records