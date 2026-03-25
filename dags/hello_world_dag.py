from airflow.decorators import dag, task
from datetime import datetime

@dag(
    dag_id="hello_world",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False
)
def hello_world():

    @task
    def say_hello():
        print("Hello depuis Airflow 3 sur Kubernetes !")

    @task
    def say_goodbye():
        print("Au revoir !")

    say_hello() >> say_goodbye()

hello_world()