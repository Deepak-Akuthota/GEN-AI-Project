from google.adk.agents import Agent
from google.adk.tools import google_search
coordinator_agent = Agent(
    name="msrit_coordinator_agent",
    model="gemini-2.5-flash",
    instruction=(
        "You are the Coordinator Agent for MSRIT, Bengaluru. "
        "You connect and synchronize all other agents — learning, admin, communication, "
        "and insight — ensuring collaboration and data sharing."
    ),
    description="Coordinates inter-agent operations within MSRIT CampusExe.",
    tools=[google_search]
)
