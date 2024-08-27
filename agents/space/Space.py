__author__ = 'Jaun van Heerden'
__email__ = 'jv.vanheerden@gmail.com'


#from agents.agent.Agent import Agent
import asyncio
import zmq
import zmq.asyncio
from typing import Dict

class Space:

    def __init__(self, name: str) -> None:
        """
        a
        """
        self.name: str = name

        self.address: str = "tcp://127.0.0.1"

        self.port: int = 5555

        self.agents: Dict = {}



    # def add_agent(self, agent: Agent) -> "Space":
    #     """
    #     a
    #     """

    #     self.agents[agent.name] = agent

    #     return self


    async def handle_agent_requests(self, socket) -> None:
        """
        Handles incoming agent requests asynchronously.
        """
        while True:
            message = await socket.recv_json()
            print(f"Received message: {message}")

            if message["type"] == "register":
                agent_name = message["name"]
                if agent_name not in self.agents:
                    agent = Agent(name=agent_name)
                    self.add_agent(agent)
                    response = {"status": "registered", "name": agent_name}
                else:
                    response = {"status": "already registered", "name": agent_name}

            elif message["type"] == "query_agents":
                response = {"status": "ok", "agents": list(self.agents.keys())}

            elif message["type"] == "send_message":
                agent_name = message["to"]
                if agent_name in self.agents:
                    self.agents[agent_name].receive_message(message["message"])
                    response = {"status": "message sent", "to": agent_name}
                else:
                    response = {"status": "agent not found", "to": agent_name}
            else:
                response = {"status": "unknown command"}

            await socket.send_json(response)


    async def run(self) -> None:
        """
        Starts the space to listen for agent connections asynchronously.
        """
        context = zmq.asyncio.Context()
        socket = context.socket(zmq.REP)  # REP-REQ pattern for request-reply
        socket.bind(f"{self.address}:{self.port}")

        print(f"{self.name} is running on {self.address}:{self.port}...")

        await self.handle_agent_requests(socket)



if __name__ == "__main__":

    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    space = Space("Space 1")

    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(space.run())
    finally:
        loop.close()

