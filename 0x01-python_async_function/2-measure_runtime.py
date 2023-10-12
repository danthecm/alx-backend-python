#!/usr/bin/env python
"""
Measure the runtime of a coroutine
"""
import time
import asyncio

wait_random = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the runtime of a coroutine
    """
    start = time.perf_counter()
    asyncio.run(wait_random(n, max_delay))
    end = time.perf_counter()
    return (end - start) / n
