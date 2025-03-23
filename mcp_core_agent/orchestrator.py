## ✅ This function will call all 3 MCP microservices in order and return a result log.

import requests

def run_sales_agent():
    try:
        # 1. Get new leads
        leads = requests.get("http://mcp_crm_connector:8000/leads/new").json()
        log = []

        for lead in leads:
            # 2. Generate email
            email_response = requests.post(
                "http://mcp_claude_email_agent:8000/generate-email",
                json=lead
            ).json()

            log.append(f"Email sent to {lead['name']}:\n{email_response.get('email', 'No email generated')}\n")

            # 3. If the lead replies "Yes", schedule a meeting
            if lead["reply"].lower() == "yes":
                schedule_response = requests.post(
                    "http://mcp_scheduler:8000/schedule",
                    json={"name": lead["name"], "email": lead["email"]}
                ).json()
                log.append(schedule_response.get("status", "Failed to schedule meeting"))
            else:
                log.append(f"No meeting scheduled for {lead['name']}.")

        return log

    except Exception as e:
        return [f"❌ Error: {str(e)}"]

