from fastapi import FastAPI
from crm_service import get_new_leads

app = FastAPI()

@app.get("/leads/new")
def fetch_new_leads():
    return get_new_leads()

# When a GET request is made to /leads/new, this returns the simulated leads.