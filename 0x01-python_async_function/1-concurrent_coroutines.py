#!/usr/bin/env python3

""" write an async routine that takes 2 int args
"""

import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Class takes 2 int args and returns list of all the delays
    """
    wait_time = await asyncio.gather(
        *list(map(lambda _: wait_random(max_delay), range(n)))
    )

    return sorted(wait_time)
