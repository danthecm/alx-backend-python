#!/usr/bin/env python3
"""
A module containing a coroutine called wait_n that takes in 2 int arguments
(max_delay and n, respectively) named wait_n that waits for a random delay
between 0 and max_delay seconds and eventually returns it.
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    A coroutine called wait_n that takes in 2 int arguments
    (max_delay and n, respectively) named wait_n that waits for a random delay
    between 0 and max_delay seconds and eventually returns it.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for i in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
