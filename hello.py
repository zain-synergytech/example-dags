from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello():
    print("Hello World from Airflow!")

with DAG(
    dag_id="hello_world",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,  # Run only when triggered manually
    catchup=False,
    tags=["example"],
) as dag:

    hello_task = PythonOperator(
        task_id="say_hello",
        python_callable=hello,
    )

    hello_task
