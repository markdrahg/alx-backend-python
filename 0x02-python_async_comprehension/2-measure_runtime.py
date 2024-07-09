#!/usr/bin/env python3
'''
Measure runtime module.
'''

import asyncio
from time import perf_counter
from typing import List
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Measures the total runtime of executing async_comprehension four times in parallel using asyncio.gather.
    Returns the total runtime in seconds.
    '''
    start_time = perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = perf_counter()
    return end_time - start_time
