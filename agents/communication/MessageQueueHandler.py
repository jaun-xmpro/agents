__author__ = 'Jaun van Heerden'
__email__ = 'jv.vanheerden@gmail.com'


import threading
import asyncio
import time


from ..communication.Message import Message


class MessageQueueHandler(threading.Thread):

    def __init__(self) -> None:
        """
        a
        """
        super().__init__()
        raise NotImplementedError("Class is not created yet")



    async def register(self, consumer: str) -> "MessageQueueHandler":
        """
        a
        """
        raise NotImplementedError("Class is not created yet")
    
        return self



    async def add_message(self, message: "Message") -> "MessageQueueHandler":
        """
        a
        """
        raise NotImplementedError("Class is not created yet")
    
        return self
