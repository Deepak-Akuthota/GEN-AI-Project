from google.adk.agents import Agent
from google.adk.tools import google_search
learning_agent = Agent(
    name="learning_agent",
    model="gemini-2.5-flash",
    instruction=(
        "You are the Learning Department Agent at MSRIT. "
        "You help manage subjects, class tests, and course recommendations."
    ),
    description="Handles learning-related tasks for MSRIT students.",
    tools=[google_search]
)
