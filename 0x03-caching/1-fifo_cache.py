#!/usr/bin/env python3
"""
FIFO caching
"""
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
    class FIFOCache that inherits from BaseCaching and is a caching system
    """

    def __init__(self) -> None:
        """Initialize class instance"""
        super().__init__()
        self.temp_cache = []

    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data for value key key
        """
        if key is not None or item is not None:
            self.cache_data[key] = item
        if key not in self.temp_cache:
            self.temp_cache.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded = self.temp_cache.pop(0)
            del self.cache_data[discarded]
            print("DISCARD: {}".format(discarded))

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key.
        """
        return self.cache_data.get(key)
