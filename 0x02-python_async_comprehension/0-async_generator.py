#!/usr/bin/env python3
""" Write a coroutine called async_generator that takes no arguments.
    The coroutine will loop x10, each time async WAIT 1 sec
    then yield a random number between 0 and 10. Use the random module.
"""


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Class that loops 10 times, wait 1 sec each time"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
