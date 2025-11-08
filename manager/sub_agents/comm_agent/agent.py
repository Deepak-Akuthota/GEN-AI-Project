from google.adk.agents import Agent
from google.adk.tools import google_search
comm_agent = Agent(
    name="msrit_comm_agent",
    model="gemini-2.5-flash",
    instruction=(
        "You are the Communication Agent for MSRIT, Bengaluru. "
        "You handle official notices, event broadcasts, and student–faculty messaging."
    ),
    description="Handles communication within MSRIT.",
    tools=[google_search]
)
