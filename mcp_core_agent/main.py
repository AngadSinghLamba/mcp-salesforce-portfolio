# Description: This file contains the FastAPI server that will run the sales agent
from fastapi import FastAPI
from orchestrator import run_sales_agent

app = FastAPI()

@app.get("/run")
def run_agent():
    return {"result": run_sales_agent()}
