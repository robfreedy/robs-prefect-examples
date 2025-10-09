from prefect import flow, get_run_logger, task
import time

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
    # To run against a local work pool called 'local-work', you would deploy this flow with:
    # prefect deployment build local/flow.py:minute_flow -n minute-flow -p local-work
    minute_flow()
