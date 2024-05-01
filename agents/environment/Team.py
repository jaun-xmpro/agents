__author__ = 'Jaun van Heerden'
__email__ = 'jv.vanheerden@gmail.com'

import threading
import queue
import time
import asyncio



from state.State import State
from communication.Message import Message
from communication.MessageQueue import MessageQueue


class Team(threading.Thread):

    def __init__(self) -> None:
        """
        a
        """

        super().__init__()

        self.state = None

        raise NotImplementedError("class is not created yet")
