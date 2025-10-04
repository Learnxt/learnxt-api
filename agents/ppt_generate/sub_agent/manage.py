from google.adk.agents import Agent
from agents.ppt_generate.sub_agent.ppt_topic_descsion_agent.agent  import ppt_topic_decision_agent
from agents.ppt_generate.sub_agent.ppt_created_agent.agent import ppt_created_agent

ppt_created_manage_agent = Agent(
    name="ppt_created_manage_agent",
    model='gemini-2.0-flash',
    description="An agent for managing PowerPoint presentations",
    instruction='''You are a PowerPoint management agent. 
    Your role is to help users with their questions and direct them to the appropriate
    specialized agent.

    first you want to confirm the topic and content with the user and ask any questionsso first go to the .
ppt_topic_decision_agent then delegate to ppt_created_manage_agent and 
go to ppt_created_agent agent to create ppt
    **Topic:**
    {topic}
    **Content:**
            {title}: [],
            {content}: [],
    ''',

    sub_agents=[
        ppt_topic_decision_agent,ppt_created_agent
    ],
    # tools=[...],
    # output_schema=ppt_created_agent
)