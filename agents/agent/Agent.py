__author__ = 'Jaun van Heerden'
__email__ = 'jv.vanheerden@gmail.com'

import threading
import queue
import time
import asyncio



from state.State import State
from communication.Message import Message
from communication.MessageQueue import MessageQueue


class Agent(threading.Thread):

    def __init__(self) -> None:
        """
        a
        """

        super().__init__()

        self.state = None

        raise NotImplementedError("Agent class is not created yet")



    def add_state(self, state: State) -> "Agent":
        """
        a
        """
        raise NotImplementedError("Agent class is not created yet")
    
        return self



    async def send_message(self, message: "Message", message_queue: "MessageQueue") -> None:
        """
        a
        """
        self.message_queues[message_queue].put(message)



    async def add_message_queue(self, name: str) -> "Agent":
        """
        a
        """
        raise NotImplementedError("Agent class is not created yet")
    
        return self