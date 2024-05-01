__author__ = 'Jaun van Heerden'
__email__ = 'jv.vanheerden@gmail.com'



from agents.agent.Agent import Agent
import asyncio

class Environment:

    def __init__(self) -> None:
        """
        a
        """
        self.agents = {}

        self.tasks = {}




    def add_agent(self, agent: Agent) -> "Environment":
        """
        a
        """

        self.agents[agent.name] = agent

        return self












    # async def add_agent(self, agent_name):
    #     """
        
    #     """
    #     if agent_name not in self.agents:
    #         agent = Agent(agent_name)
    #         self.agents[agent_name] = agent
    #         task = asyncio.create_task(agent.run())
    #         self.tasks[agent_name] = task
    #         print(f"Added agent {agent_name}")
    #     else:
    #         print(f"Agent {agent_name} already exists.")


    # def remove_agent(self, agent_name):
    #     """
        
    #     """
    #     if agent_name in self.agents:
    #         self.agents[agent_name].stop()
    #         # Await the task to be completed if needed or cancel it
    #         self.tasks[agent_name].cancel()
    #         del self.agents[agent_name]
    #         del self.tasks[agent_name]
    #         print(f"Removed agent {agent_name}")
    #     else:
    #         print(f"Agent {agent_name} does not exist.")
















    # async def start_all(self):
    #     """
        
    #     """
    #     for agent in self.agents:
    #         task = asyncio.create_task(self.agents[agent].run())
    #         self.tasks[agent] = task