#!/usr/bin/env python3
"""
This module contains an asynchronous generator named async_generator.
The purpose of async_generator is to demonstrate asynchronous programming
by yielding a random number between 0 and 10 after waiting for 1 second,
repeating this process 10 times.
"""

import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronous generator that yields a random number between 0 and 10.
    
    The generator waits for 1 second before yielding each number,
    demonstrating asynchronous behavior. This process is repeated
    10 times.
    
    Returns:
        Generator[float, None, None]: A generator yielding random floats.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

