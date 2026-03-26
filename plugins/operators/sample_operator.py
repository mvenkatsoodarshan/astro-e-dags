import logging
from airflow.models.baseoperator import BaseOperator
from hooks.sample_hook import SampleHook

class SampleOperator(BaseOperator):
    """
    A simple custom operator that interacts with the SampleHook to fetch data.
    """
    template_fields = ('endpoint',)

    def __init__(
        self,
        sample_conn_id: str,
        endpoint: str,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.sample_conn_id = sample_conn_id
        self.endpoint = endpoint

    def execute(self, context):
        logging.info(f"Starting SampleOperator execution for endpoint: {self.endpoint}")
        
        # Instantiate the custom hook
        hook = SampleHook(sample_conn_id=self.sample_conn_id)
        
        # Call a method from the hook to get data
        result = hook.fetch_data(endpoint=self.endpoint)
        
        logging.info(f"Data retrieved successfully: {result}")
        
        # In Airflow, returning a value from `execute` will automatically push it to XCom
        return result
