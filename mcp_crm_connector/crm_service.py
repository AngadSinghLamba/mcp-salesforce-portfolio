def get_new_leads():
    return [
        {
            "name": "Alice Smith",
            "company": "HealthTech Inc.",
            "industry": "Healthcare",
            "email": "alice@healthtech.com",
            "reply": "Yes"   # Simulated response
        },
        {
            "name": "John Doe",
            "company": "FinSmart",
            "industry": "Finance",
            "email": "john@finsmart.com",
            "reply": "No"
        }
    ]

## This function simulates two "new" leads from a CRM. Later, this will be replaced with an actual Salesforce API call.