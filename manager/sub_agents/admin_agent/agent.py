from google.adk.agents import Agent
from google.adk.tools import google_search
admin_agent = Agent(
    name="admin_agent",
    model="gemini-2.5-flash",
    instruction=(
        "You are the Administration Agent for MSRIT. "
        "You schedule exams, manage classrooms, and handle campus logistics."
    ),
    description="Manages scheduling and resources for MSRIT.",
    tools=[google_search]
)
