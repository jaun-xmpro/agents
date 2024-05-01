__author__ = 'Jaun van Heerden'
__email__ = 'jv.vanheerden@gmail.com'


import queue
import time
import asyncio


from ..communication.Message import Message
from ..communication.MessageQueue import MessageQueue

from ..monitoring.Logging import setup_logging




class AgentThread:

    def __init__(self, name: str) -> None:
        """
        a
        """
        self.name = name
    

    def start(self):
        """
        a
        """
        raise NotImplementedError("Class is not created yet")
    
    def stop(self):
        """
        a
        """
        raise NotImplementedError("Class is not created yet")


    def end(self):
        """
        a
        """
        raise NotImplementedError("Class is not created yet")
    

    async def loop(self):

        while True:
            asyncio.sleep(10)
            print(f"Agent {self.name} is still running.")



class Agent:

    def __init__(self, name=None) -> None:
        """
        a
        """
        if name is None:
            name = "Agent"

        self.name = name

        self._running = False

        self.message_queues = {"_default": MessageQueue()}

        self.threads = {}

        self.logger = setup_logging()
        self.logger.info(f"Agent initialized with default message queue.")

        
    async def run(self):
        """
        
        """
        self._running = True
        self.logger.info("Agent started running.")



    async def send_message(self, message: "Message", message_queue_name: str = '_default') -> None:
        """
        a
        """
        await self.message_queues[message_queue_name].message_queue.put(message)
        self.logger.info(f"Message[{[message.recipients]}] added to message queue {message_queue_name}.")



    async def add_thread(self, thread: AgentThread) -> "Agent":
        """
        a
        """

        thread = asyncio.create_task(thread.run())

        self.threads[thread.name] = thread




















    # def run_threads(self):
    #     """
        
    #     """

    #     for thread in self.threads:
    #         self.threads[thread].start()

    #     self.logger.info("Threads started.")



















    # async def loop(self):
    #     """
        
    #     """

    #     while True:

    #         if self._running:

    #             self.


    #         await asyncio.sleep(10)
    #         self.logger.info("Agent is still running.")



        # while self._running:
        #     await asyncio.sleep(10)
        #     self.logger.info("Agent is still running.")






    # def stop(self):
    #     """
        
    #     """
    #     self._running = False
    #     self.logger.info("Agent stopping...")

    #     self.inbox.put_nowait("STOP")  # Trigger the queue to unblock if waiting