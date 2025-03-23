# Description: This file contains the FastAPI application that will be used to generate emails.
from fastapi import FastAPI, Body
from email_generator import generate_email

app = FastAPI()

@app.post("/generate-email")
def generate(payload: dict = Body(...)):
    name = payload.get("name")
    company = payload.get("company")
    industry = payload.get("industry")

    if not name or not company or not industry:
        return {"error": "Missing required fields"}

    email = generate_email(name, company, industry)
    return {"email": email.strip()}
