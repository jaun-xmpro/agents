__author__ = 'Jaun van Heerden'
__email__ = 'jv.vanheerden@gmail.com'



from Thread import Thread

import asyncio
import time

class Message:

    def __init__(self) -> None:
        """
        a
        """
        raise NotImplementedError("Class is not created yet")




    async def set_sender(self, sender):
        """

        """
        self.sender = sender



    async def set_recipient(self, recipient):

        self.recipient = recipient
        
    
    
    async def add_thread(self, thread: Thread) -> "Message":
        """
        a
        """
        raise NotImplementedError("Class is not created yet")
    
        return self
    


    async def add_content(self, content) -> "Message":
        """
        a
        """
        raise NotImplementedError("Class is not created yet")
    
        return self
    
        self.content = content



