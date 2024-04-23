#!/usr/bin/env python3
""" Write a coroutine called async_comprehension that takes no args
    The coroutine will collect 10 random numbs using an async comprehensing
    over async_generator, then return the 10 random numbers.
"""


from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Class that collects 10 random numbs and returns themusing async comp"""
    collectRandom_numbs = [i async for i in async_generator()]
    return collectRandom_numbs
