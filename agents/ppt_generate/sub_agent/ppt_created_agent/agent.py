# ppt_created_agent
from google.adk.agents import Agent
from pydantic import BaseModel, Field

class ppt_created_agent_class(BaseModel):
    no_of_slides: int = Field(..., description='Number of slides in the presentation')
    topic_name: str = Field(..., description='Name of the presentation')
    title: list[str] = Field(..., description='Title of the slides')
    content: list[str] = Field(..., description='Content of the slides')


ppt_created_agent = Agent(
    name="ppt_created_agent",
    model='gemini-2.0-flash',
    description="An agent for creating PowerPoint presentations",
    instruction='''You are a PowerPoint creation agent. 
    Your task is to assist users in creating PowerPoint presentations. 
    You can create new slides, add content to slides, and remove slides as needed. 
    Always follow the user's instructions carefully and ask clarifying questions if needed.
    **Topic:**
    {topic}
    **Content:**
            {title}: [],
            {content}: [],
    ''',
    # tools=[...],
    output_schema=ppt_created_agent_class
)