#!/usr/bin/evn python3
"""provides the class, BasicCache"""
from basic_caching import BaseCaching


class BasicCache(BaseCaching):
    """A simple key-value cache with a fixed maximum size."""

    def put(self, key, item):
        """Add an item to the cache with a given key"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache by its key"""
        return self.cache_data.get(key)
