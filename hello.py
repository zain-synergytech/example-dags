from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def hello():
    print("Hello World from Airflow!")

with DAG(
    dag_id="hello_world",
    catchup=False,
    tags=["example"],
) as dag:

    hello_task = PythonOperator(
        task_id="say_hello",
        python_callable=hello,
    )

    hello_task
