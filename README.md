CAMPUS EXE 
-A Multi-Agent AI System for MSRIT
========================

CampusExe is a multi-agent AI system built with the Google Agent Development Kit (ADK),
customized for M. S. Ramaiah Institute of Technology (MSRIT), Bengaluru.

It acts as an intelligent assistant for the campus, using a team of specialized AI agents
to handle tasks related to academics, administration, and communication.



🤖 HOW IT WORKS: AGENT ARCHITECTURE


The system uses a hierarchical agent architecture.
A main "Manager" agent receives a request and intelligently delegates it to the
correct specialized sub-agent to get the job done.



Root Agent (The Manager)

msrit_campus_manager_agent
File: manager/agent.py

Description:
This is the main entry point and coordinator.
It understands a user's request and routes it to the correct sub-agent for handling.



Sub-Agents (The Specialists)


🎓 learning_agent
-----------------
Description:
Helps students and faculty with academic tasks.

Responsibilities:
- Manages information on subjects, class tests, and course recommendations.


🏛️ admin_agent
-----------------
Description:
Handles campus logistics and administrative operations.

Responsibilities:
- Schedules exams
- Manages classroom assignments
- Handles resource booking


💬 msrit_comm_agent (Communication Agent)
----------------
Description:
Manages all official campus communication.

Responsibilities:
- Broadcasts official notices
- Sends event announcements
- Facilitates student-faculty messaging


📊 msrit_insight_agent
-----------------------
Description:
The data analysis expert.

Responsibilities:
- Analyzes academic and administrative data
- Provides reports and identifies trends


🤝 msrit_coordinator_agent
---------------------------
Description:
Ensures all agents work together smoothly.

Responsibilities:
- Synchronizes operations
- Enables data sharing between learning, admin, communication, and insight agents



🛠️ TECH STACK


Core Framework:  Google Agent Development Kit (ADK)
AI Model:        gemini-2.5-flash
Tools:           Google Search (used by sub-agents)
Cloud Platform:  Google Cloud AI Platform (Vertex AI)
Language:        Python



🚀 GETTING STARTED


-------------------------
PREREQUISITES & INSTALLATION
-------------------------

Core Requirements:
- Python 3.10+
- A Google Cloud project with Vertex AI API enabled


1. Clone the repository:
------------------------
git clone https://github.com/your-username/campusexe.git
cd campusexe


2. Set up a virtual environment:
-------------------------------
python -m venv .venv

# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate


3. Install Python Dependencies:
-------------------------------
Create a file named "requirements.txt" in the root folder with the following content:

--------------------------------
google-adk>=0.5.2
google-cloud-aiplatform>=1.63.0
python-dotenv
--------------------------------

Then run:
pip install -r requirements.txt


4. Configure Environment Variables:
-----------------------------------
(If the .env file is missing, you must create it manually.)

Create a file named ".env" in the project's root folder and add the following:

--------------------------------
GOOGLE_CLOUD_PROJECT="your-project-id"
GOOGLE_CLOUD_LOCATION="your-region"   # e.g., us-central1
--------------------------------

▶️ RUNNING THE AGENT
======================

You can start and interact with the main manager agent using the ADK CLI.
(This assumes your agents are correctly defined in your pyproject.toml file.)

Command:
---------
adk run manager


END OF FILE
============================================================



