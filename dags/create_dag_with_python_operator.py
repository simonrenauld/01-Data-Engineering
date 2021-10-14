from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator


default_args = {
    'owner':'simon',
    'retries': 5, 
    'retry_delay': timedelta(minutes=5)
}

def greet():
    print("Hello World")

with DAG(
    default_args=default_args,
    dag_id='dag_with_python_operator_V01',
    description='dag using python operators',
    start_date=datetime(2021,10,13)
) as dag: 
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet
    )