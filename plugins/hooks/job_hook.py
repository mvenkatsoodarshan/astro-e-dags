import sqlite3
from airflow.hooks.base import BaseHook

class JobHook(BaseHook):

    def get_new_records(self, last_id):
        conn = sqlite3.connect("test.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM jobs WHERE id > ?", (last_id,)
        )

        rows = cursor.fetchall()
        conn.close()

        return rows