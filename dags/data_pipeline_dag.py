from datetime import datetime
from scripts.extract import extract_data
from scripts.transform import preprocess_text
from scripts.store import store_data

from airflow import DAG
from airflow.operators.python_operator import PythonOperator

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 5, 7),
}

dag = DAG(
    "data_pipeline",
    default_args=default_args,
    description="A DAG to automate data extraction, transformation, and storage",
    schedule_interval="0 0 * * *",  # Run daily at midnight
)

extract_task = PythonOperator(
    task_id="extract_data",
    python_callable=extract_data,
    dag=dag,
)

transform_task = PythonOperator(
    task_id="transform_data",
    python_callable=preprocess_text,
    dag=dag,
)

store_task = PythonOperator(
    task_id="store_data",
    python_callable=store_data,
    dag=dag,
)

extract_task >> transform_task >> store_task
