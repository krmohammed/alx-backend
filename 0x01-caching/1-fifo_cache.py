#!/usr/bin/env python3
"""provides the class FIFOCache"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache class"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache and remove the oldest item if necessary"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            oldest_key = next(iter(self.cache_data))
            del self.cache_data[oldest_key]
            print("DISCARD: {}".format(oldest_key))
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None:
            return None
        return self.cache_data.get(key)
