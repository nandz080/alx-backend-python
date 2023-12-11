#!/usr/bin/env python3
""" Module that takes an int and returns a asynio.Task
"""

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Class  that creates an async task for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
