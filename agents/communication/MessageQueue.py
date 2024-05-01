__author__ = 'Jaun van Heerden'
__email__ = 'jv.vanheerden@gmail.com'


import threading
import asyncio
import time

from ..communication.Message import Message
from ..communication.MessageQueueHandler import MessageQueueHandler



class MessageQueue(threading.Thread):

    def __init__(self) -> None:
        """
        a
        """
        super().__init__()
        
        self.message_queue_handlers: dict = {}

        self.message_queue = asyncio.Queue()



    async def register_to(self, message_queue_handler: "MessageQueueHandler") -> "MessageQueue":
        """
        a
        """
        raise NotImplementedError("Class is not created yet")
    
        return self



    async def add_message(self, message: "Message") -> "MessageQueueHandler":
        """
        a
        """
        
        await self.broadcast(message)




    async def broadcast(self, message: "Message") -> tuple[int, int]:
        """
        a
        """

        success = 0
        total = len(self.message_queue_handlers)

        for message_queue_handler in self.message_queue_handlers:
            await message_queue_handler.add_message(message)
        
        return (success, total)