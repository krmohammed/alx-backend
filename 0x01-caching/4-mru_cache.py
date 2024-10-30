#!/usr/bin/env python3
"""MRU Cache"""

BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """MRU Cache Implementation"""

    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Adds an item to the cache
        based on MRU algorithm
        """
        if key is None or item is None:
            return
        size = len(self.cache_data)
        if key not in self.cache_data and size >= BaseCaching.MAX_ITEMS:
            recent = self.order.pop(0)
            self.cache_data.pop(recent)
            print(f"DISCARD: {recent}")
        self.cache_data[key] = item

        if key in self.order:
            self.order.remove(key)
            self.order.insert(0, key)
        else:
            self.order.insert(0, key)

    def get(self, key):
        """Get an item by key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        self.order.remove(key)
        self.order.insert(0, key)
        return self.cache_data.get(key)
