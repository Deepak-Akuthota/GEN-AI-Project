from google.adk.agents import Agent
from google.adk.tools import agent_tool   
from .sub_agents.learning_agent import learning_agent
from .sub_agents.admin_agent import admin_agent
from .sub_agents.comm_agent import comm_agent
from .sub_agents.insight_agent import insight_agent

root_agent = Agent(
    name="msrit_campus_manager_agent",
    model="gemini-2.5-flash",
    instruction=(
        "You are the Campus Manager Agent for M. S. Ramaiah Institute of Technology, Bengaluru, Karnataka. "
        "You coordinate and delegate tasks to sub-agents for learning, administration, communication, "
        "and insights. Decide which sub-agent to use and provide a clear response."
    ),
    description="Root agent coordinating MSRIT sub-agents.",
    tools=[
        agent_tool.AgentTool(agent=learning_agent),
        agent_tool.AgentTool(agent=admin_agent),
        agent_tool.AgentTool(agent=comm_agent),
        agent_tool.AgentTool(agent=insight_agent),
    ]
)
