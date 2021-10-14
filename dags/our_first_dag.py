from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'simon',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='first_dag_v3',
    default_args=default_args,
    description='This is our first dag that we write',
    start_date=datetime(2021, 11, 11, 2),
    schedule_interval='@daily'

) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command="echo hello world, this is the first task"
    )

    task2 = BashOperator(
        task_id='second_task',
        bash_command="echo hello world, I am task2 i will be running after task1"
    )

    task3 = BashOperator(
        task_id='third_task',
        bash_command="this is task 3, running at same time of task 2"
    )


    task1.set_downstream(task2)
    task1.set_downstream(task3)