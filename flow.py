from prefect import flow, get_run_logger
from prefect.context import FlowRunContext

@flow
def my_flow():
    logger = get_run_logger()
    logger.info("Hello, world!")
    logger.info(FlowRunContext.get())

if __name__ == "__main__":
    my_flow()