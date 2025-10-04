# from agent.call_agent import class_agent,create_sections
import asyncio
from agents.call_agent import class_agent,create_sections


async def main():
    agent_types=['doubt_clear','ppt']
    print("Welcome to Buddy!\nThis is an AI-powered agent for creating ppt.")
    print("Please enter your query to get started.")
    await create_sections()
    while True:
        user_query = input("Query: ")
        if user_query.lower() == "exit":
            print("Exiting Buddy. Goodbye!")
            break
        print(f"[~User~]: {user_query}")
        await class_agent(user_query,agent_type=agent_types[0])


if __name__ == "__main__":
    asyncio.run(main())

