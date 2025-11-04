from prefect import flow, task

@task
def say_hello(name: str) -> str:
    return f"Hello, {name}!"

@flow
def hello_flow():
    greeting = say_hello("Prefect 3")
    print(greeting)

if __name__ == "__main__":
    hello_flow()
