#!/usr/bin/env python3
""" Write a  measure_runtime coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather. Measure_runtime should 
    measure the total runtime and return it.
"""


import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Class that that executes async 4 times and measure the total runtime"""
    startTime = time.time()

    await asyncio.gather(*(async_comprehension() for i in range(4)))

    endTime = time.time()
    totalRunTime = endTime - startTime
    return totalRunTime
