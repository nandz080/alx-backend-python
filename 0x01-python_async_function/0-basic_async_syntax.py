#!/usr/bin/env python3
"""Write an asynchronous coroutine that takes in an integer arg
    
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """ Generator that yields a random value between 0 and 10 every second,
        10 times"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
