from prefect import flow, get_run_logger
from prefect import runtime

@flow
def my_flow():
    logger = get_run_logger()
    logger.info("Hello, world!")
    logger.info(runtime.deployment)

if __name__ == "__main__":
    my_flow()