# mcp-salesforce-portfolio
Sales Pipeline using MCP 


✅ Step 1: Create the Project Structure for the MCP Virtual Sales Assistant

🎯 What We're Doing in This Step:
We're setting up the foundation of our project by creating a folder structure that follows the MCP-style microservice architecture.

Each folder will represent a separate MCP server, responsible for one part of the Virtual Sales Assistant workflow:

Getting leads

Generating cold emails

Scheduling meetings

Orchestrating the flow

This structure will help us:

Keep each server focused and modular

Run each module as its own Dockerized FastAPI microservice

Plug them together later using docker-compose


✅ Step 2: Create the mcp_crm_connector MCP Server

🎯 What We’re Doing in This Step
We’re going to build a microservice that simulates retrieving new sales leads. This server will act as our CRM data connector, similar to how a real Salesforce integration would work in a production system.

This is your first real MCP server, which:

Runs as a FastAPI web server

Has a single endpoint: GET /leads/new

Returns a list of mock leads

Will be called by the MCP Core Agent later

This server simulates a local data source or remote CRM (like Salesforce) — in a real setup, you could replace this with an API call to Salesforce using simple-salesforce.


✅ Step 3: Create the mcp_claude_email_agent MCP Server

🎯 What We’re Doing in This Step:
We're building the Claude Email Generator as its own MCP server.
This module will:

Be a FastAPI microservice

Expose a POST endpoint: /generate-email

Accept a lead's name, company, and industry as input

Return a personalized cold email (generated using a mock Claude response for now)

Later, you’ll be able to plug this into:

Claude Desktop (via clipboard or Claude API)

Other LLMs (OpenAI, Azure OpenAI, etc.)

Or any custom prompt engine

✅ Step 4: Create the mcp_scheduler MCP Server

🎯 What We’re Doing in This Step:

We’re building the third MCP server:
➡️ mcp_scheduler — it simulates booking meetings with leads who responded positively.

This server will:

Be a FastAPI microservice

Expose one POST endpoint: /schedule

Accept lead details (name, email)

Return a simulated meeting confirmation

Later, this can be upgraded to integrate with Google Calendar or Outlook via API

✅ Step 5: Create the mcp_core_agent MCP Server (The Orchestrator)

🎯 What We’re Doing in This Step:
We’re building the MCP Core Agent, which acts as the brain of your Virtual Sales Assistant.

It will:

Call the CRM connector to get leads

Send each lead to the email generator

Schedule a meeting if the lead's reply is "Yes"

This is where the agentic workflow logic lives — it knows what to do, in what order, and when.

