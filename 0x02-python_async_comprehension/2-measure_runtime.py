#!/usr/bin/env python3
"""
This module demonstrates measuring the runtime of executing multiple
asynchronous comprehensions in parallel.
"""

import asyncio
import time
from async_comp_module import async_comprehension

async def measure_runtime() -> float:
    """
    Measures and returns the total runtime of executing the async_comprehension
    coroutine four times in parallel.
    
    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.time()

    return end_time - start_time

