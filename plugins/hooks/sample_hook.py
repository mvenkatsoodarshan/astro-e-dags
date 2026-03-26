import logging
from airflow.hooks.base import BaseHook

class SampleHook(BaseHook):
    """
    A simple custom hook example showing how to connect to an external system.
    """
    def __init__(self, sample_conn_id: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sample_conn_id = sample_conn_id

    def get_conn(self):
        """
        In a real hook, this would return a connection to an external system
        (e.g., requests.Session, database cursor, etc.).
        """
        # In Airflow 2.x, the proper way to get connection details from Airflow database:
        # conn = self.get_connection(self.sample_conn_id)
        # return conn
        
        logging.info(f"Retrieving connection details for {self.sample_conn_id}")
        return {"status": "connected", "conn_id": self.sample_conn_id}

    def fetch_data(self, endpoint: str):
        """
        Simulate fetching data from an external API endpoint.
        """
        conn = self.get_conn()
        logging.info(f"Using connection: {conn} to fetch data from endpoint: {endpoint}")
        return {"data": ["apple", "banana", "cherry"], "endpoint": endpoint}
