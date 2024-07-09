#!/usr/bin/env python3
"""
Module containing an asynchronous comprehension function.
"""

import asyncio
from typing import List
import importlib.util


spec = importlib.util.spec_from_file_location('async_generator', '0-async_generator.py')
async_generator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(async_generator)

async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension over async_generator.

    Returns:
        A list of 10 random float numbers.
    """
    return [i async for i in async_generator.async_generator()]
