# Description: This file contains the FastAPI code that will be used to create the API endpoint for the agent.
from fastapi import FastAPI, Body
from scheduler import schedule_meeting

app = FastAPI()

@app.post("/schedule")
def schedule(payload: dict = Body(...)):
    name = payload.get("name")
    email = payload.get("email")

    if not name or not email:
        return {"error": "Missing required fields"}

    result = schedule_meeting(name, email)
    return {"status": result}
