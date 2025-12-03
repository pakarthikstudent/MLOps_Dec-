from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

## task-1 push a value(data) to XCom

def f1(**kwargs):
    value_to_push = "Test data from f1 block"
    kwargs["K1"]=xcom_push(key="my_key",value=value_to_push)

## task-2 pull a value from XCom

def f2(**kwargs):
    value_from_xcom = kwargs["K1"].xcom_pull(task_ids="f1",key="my_key")
    print(f"pulled value from XCom:{value_from_xcom}")

## default args
default_args = {
        'owner': 'airflow',
        'start_date':datetime(2025,12,3),
        'retries':1
}
## define the DAG
dag = DAG(
        'task-to-task-demo',
        default_args = default_args,
        schedule_interval='@daily',
)

task1 = PythonOperator(
        task_id='push-f1',
        python_callable=f1,
        provide_context=True,
        dag=dag,
        )

task2 = PythonOperator(
        task_id='pull-f2',
        python_callable=f2,
        provide_context=True,
        dag=dag,
        )

## set the task dependencies
task1 >> task2
