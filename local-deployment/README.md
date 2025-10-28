# Local Deployment Guide

This guide will help you set up a local Python environment using [uv](https://github.com/astral-sh/uv), install dependencies, run your Prefect flow, and start a Prefect local worker for a work pool named `local-work`.

## 1. Create a uv Virtual Environment

If you don't have `uv` installed, follow the [installation instructions](https://github.com/astral-sh/uv#installation).

Create a new virtual environment in the current directory:

```bash
uv venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

## 2. Login to Prefect Cloud

```
prefect cloud login
```

## 3. Start a local worker

When a process worker is started, a process work pool is automatically created in Prefect Cloud if it does not exist already

```
prefect worker start --type process --pool local-work
```

## 4. Deploy your flow

In a new terminal, run the flow.py file, which creates a deployment pointed to the local-work worker

```python
python flow.py
```