from airflow.decorators import dag, task
from datetime import datetime
import socket

@dag(
    dag_id="test_cluster_connectivity",
    schedule=None,
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["debug"],
)
def debug_workers():

    @task(queue="default") # Usamos 'default' para asegurar que el worker lo vea
    def check_identity(task_number: int):
        hostname = socket.gethostname()
        ip_addr = socket.gethostbyname(hostname)
        print(f"¡Hola! Soy la tarea #{task_number}")
        print(f"Estoy ejecutándome en el Worker: {hostname}")
        print(f"Mi IP privada es: {ip_addr}")
        return f"Worker {hostname} reportándose."

    # Lanzamos 6 tareas para que se repartan entre los workers
    for i in range(1, 7):
        check_identity(i)

debug_workers_dag = debug_workers()