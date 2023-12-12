#!/usr/bin/env python3
""" Write an asynchronous coroutine that takes in an integer
    argument named wait_random that waits for a random delay 
    between 0 and max_delay seconds and eventually returns
    it
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Class that waits for a random number of seconds
    """
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
