from prefect import flow, get_run_logger, task
from pathlib import Path
import time
from prefect.schedules import Cron

@task
def long_task():
    logger = get_run_logger()
    logger.info("Starting a 60-second task...")
    time.sleep(60)
    logger.info("Finished the 60-second task.")

@flow
def minute_flow():
    logger = get_run_logger()
    logger.info("Flow started. Will run a task that takes about a minute.")
    long_task()
    logger.info("Flow finished.")

if __name__ == "__main__":
    minute_flow.from_source(
        source=str(Path(__file__).parent),
        entrypoint="flow.py:minute_flow",
    ).deploy(
        name="minute-deployment",
        work_pool_name="local-work",
        schedule=Cron("10 * * * *")
    )
    # minute_flow()