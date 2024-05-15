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


    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """method get"""
        value = self._redis.get(key)
        if value is None:
            return
        if fn is int:
            return self.get_int(value)
        if fn is str:
            return self.get_str(value)
        if fn is None:
            return value
        return fn(value)

    def get_str(self, data: bytes) -> str:
        """method get_str"""
        return data.decode("utf-8")

    def get_int(self, data: bytes) -> int:
        """method get_int"""
        return int(data)
