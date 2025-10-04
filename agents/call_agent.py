import uuid
import asyncio
import json
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from requests import session
from .ppt_generate.sub_agent.manage import ppt_created_manage_agent
from .ppt_generate.sub_agent.ppt_created_agent.ppt_generate import ppt_generate_class
from .note_creater.doubt_clear_agent import doubt_clear_agent

load_dotenv()


# Create a new session service to store state
session_service_stateful = InMemorySessionService()

initial_state = {
    'no_of_slides': 0,
    'topic': '',
    'title': [],
    'content': [],
}

# Create a NEW session
APP_NAME = "buddy"
USER_ID = "buddy"
SESSION_ID = str(uuid.uuid4())




async def create_sections():
    stateful_session = await session_service_stateful.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID,
        state=initial_state,
    )
    print("CREATED NEW SESSION:")
    print(f"\tSession ID: {SESSION_ID}")


async def class_agent(userPrompt,agent_type):

    # select Agents types
    if agent_type=='ppt':
        runner = Runner(
        agent=ppt_created_manage_agent,
        app_name=APP_NAME,
        session_service=session_service_stateful,
    )
    elif agent_type == 'doubt_clear':
        runner = Runner(
        agent=doubt_clear_agent,
        app_name=APP_NAME,
        session_service=session_service_stateful,
    )
    
    print("==== Subagent ====")
    print(f"agent is running...")

    new_message = types.Content(
        role="user", parts=[types.Part(text=userPrompt)]
    )

    for event in runner.run(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=new_message,
    ):
        # select agent types to get final respones
        if agent_type=='ppt':
            if event.is_final_response():
                if event.content and event.content.parts:
                    print(f"Final Response: {event.content.parts[0].text}")
                    try:
                        output = event.content.parts[0].text
                        data_dict = json.loads(output)
                    # print("Updated state:", isinstance(data_dict, dict))
                        if isinstance(data_dict, dict):
                            # initial_state.update(data_dict)
                            ppt_generate_instance = ppt_generate_class(
                            no_of_slides=data_dict.get('no_of_slides', 0),
                            topic_name=data_dict.get('topic_name', ''),
                            title=data_dict.get('title', ''),
                            content=data_dict.get('content', '')
                        ).generate_ppt()
                            print("Updated state:", isinstance(data_dict, dict))
                        print("Updated state:", isinstance(data_dict, dict))


                    except Exception as e:
                        print(f"Error parsing output: {e}"),
    
        elif agent_type == 'doubt_clear':
            if event.is_final_response():
                if event.content and event.content.parts:
                    print(f"Final Response: {event.content.parts[0].text}")
                    try:
                        output = event.content.parts[0].text
                        data_dict = json.loads(output)
                    # print("Updated state:", isinstance(data_dict, dict))
                        if isinstance(data_dict, dict):
                        # initial_state.update(data_dict)
                        #     ppt_generate_instance = ppt_generate_class(
                        #     no_of_slides=data_dict.get('no_of_slides', 0),
                        #     topic_name=data_dict.get('topic_name', ''),
                        #     title=data_dict.get('title', ''),
                        #     content=data_dict.get('content', '')
                        # ).generate_ppt()
                            print("Updated state:", isinstance(data_dict, dict))


                    except Exception as e:
                        print(f"Error parsing output: {e}")
        

    print("==== Session Event Exploration ====")
    session = await session_service_stateful.get_session(
        app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID
    )

    # Log final Session state
    print("=== Final Session State ===")
    for key, value in session.state.items():
        print(f"{key}: {value}")