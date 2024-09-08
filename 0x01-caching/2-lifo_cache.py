#!/usr/bin/env python3
"""provides the class LIFOCache"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class"""

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add an item to the cache
        Args:
            key (str): the unique identifier for the item
            item (any): the item to store
        """
        if len(self.cache_data) >= self.MAX_ITEMS:
            k, v = self.cache_data.popitem()
            print("DISCARD: {}".format(k))
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key
        Args:
            key (str): the unique identifier for the item
        Returns:
            any: the item associated with the key, or None if not found
        """
        if key is None:
            return None
        return self.cache_data.get(key)
