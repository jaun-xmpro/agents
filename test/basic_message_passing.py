
import asyncio


async def main():

    env = Environment()

    agent_1 = Agent()
    agent_2 = Agent()

    env.add_agent(agent_1)
    env.add_agent(agent_2)

    message = Message()

    message.add_recipient(agent_1)

    await agent_2.send_message(message)
    



if __name__ == "__main__":

    from agents.agent.Agent import Agent
    from agents.environment.Environment import Environment
    from agents.communication.Message import Message

    asyncio.run(main())



