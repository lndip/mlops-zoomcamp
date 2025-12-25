import logging
from prefect import flow, task

@task 
def say_hello():
    logging.info("Hello from a running task")
    return "hello completed"

@flow(name="hello-flow")
def hello_flow():
    logging.info("Starting the flow")
    result = say_hello()
    logging.info(f"Task result: {result}")

if __name__ == "__main__":
    hello_flow()

'''
flow run: 1 execution of the flow
deployment: only creates flow runs
worker: actually executes flow runs

    if 
    (prefect server start
    prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api):
=>  Prefect Server (API)
        ↑
    Prefect client (your code)
        ↓
    Worker processes
    else:
    Python process
    └─ Prefect logic (temporary, in-memory) => No client, server architecture

1. Test locally without deployment
    python hello_prefect.py

2. Deploy flow to Prefect Server
    prefect deploy hello_prefect.py:hello_flow -n ... -p ...
Answer prompts: name, pool, infrastructure, schedule, etc.

3. Start a worker for the deployment
    prefect worker start --pool <pool-name>

# 4. Trigger flow immediately
    prefect deployment run hello-flow/<deployment-name>

# 5. Optional: scheduled runs will also be executed automatically
'''