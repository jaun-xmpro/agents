__author__ = 'Jaun van Heerden'
__email__ = 'jv.vanheerden@gmail.com'



# from Thread import Thread

import asyncio
import time


from ..monitoring.Logging import setup_logging


class Message:

    def __init__(self) -> None:
        """
        a
        """
    
        self.read = False
        self.recipients = {}

        self.logger = setup_logging()



    async def set_sender(self, sender):
        """

        """
        self.sender = sender



    def add_recipient(self, recipient):
        """

        """
        self.logger.debug(f"Adding recipient {recipient.name} to message {self.name}")
        self.recipients[recipient.name] = recipient
        
    
    
    # async def add_thread(self, thread: Thread) -> "Message":
    #     """
    #     a
    #     """
    #     raise NotImplementedError("Class is not created yet")
    
    #     return self
    


    async def add_content(self, content) -> "Message":
        """
        a
        """
        raise NotImplementedError("Class is not created yet")
    
        return self
    
        self.content = content



