#!/usr/bin/env python3
"""Basic Cache"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """Basic Cache Implementation"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Adds an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)
