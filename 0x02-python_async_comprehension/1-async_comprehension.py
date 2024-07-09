#!/usr/bin/env python3
'''Task 1's module.
'''
import asyncio
from typing import List
from async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehension over async_generator.
    
    Returns:
        A list of 10 random float numbers.
    """
    return [i async for i in async_generator()]
