from fastapi import FastAPI
# from fastapi.responses import HTMLResponse
from agents.call_agent import class_agent,create_sections


app = FastAPI(
    title="LearnXT-API",
    description="LearnXT-API for ai generate content",
    version="0.1.0",
)

@app.get('/')
def createsection():
    create_sections()

@app.get('chat/{agent_type}/{promt}')
def leanxt(agent_type:int,promt:str):
    agent_types=['doubt_clear','ppt']
    class_agent(promt,agent_type=agent_types[0])
    pass
