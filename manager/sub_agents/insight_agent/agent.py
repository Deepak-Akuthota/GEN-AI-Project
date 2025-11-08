from google.adk.agents import Agent
from google.adk.tools import google_search
insight_agent = Agent(
    name="msrit_insight_agent",
    model="gemini-2.5-flash",
    instruction=(
        "You are the Insight Agent for MSRIT, Bengaluru. "
        "You analyze academic, administrative, and event data to provide useful insights "
        "and trends. Use google_search when you need external benchmarks or reports "
        "for comparison."
    ),
    description="Provides data-driven insights for MSRIT.",
    tools=[google_search]
)
