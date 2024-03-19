#!/usr/bin/env python3
"""
Module measure_runtime demonstrates measuring the execution time of
running multiple asynchronous comprehensions in parallel, highlighting
the efficiency and concurrency of asynchronous operations in Python.
"""

import asyncio
import time
from typing import float
# Assuming async_comprehension is in the same directory. Adjust import as necessary.
from async_comprehension import async_comprehension

async def measure_runtime() -> float:
    """
    Measures the runtime of executing async_comprehension four times
    in parallel and returns the total execution time.

    Returns:
        float: The total execution time in seconds.
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

