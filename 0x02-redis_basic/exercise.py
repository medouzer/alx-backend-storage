#!/usr/bin/env python3
"""Writing strings to Redis"""

import uuid
from typing import Union
import redis


class Cache:
    """class Cache"""
    def __init__(self):
        """init new object"""
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        """store data"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
