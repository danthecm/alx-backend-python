#!/usr/bin/env python3
"""
A module containing a coroutine called wait_random that takes in an integer
argument (max_delay, with a default value of 10) named wait_random that waits
for a random delay between 0 and max_delay seconds and eventually returns it.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that takes in an integer argument (max_delay)
    and returns a random float value after waiting for a random delay between
    0 and max_delay seconds."""
    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
