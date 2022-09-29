#!/usr/bin/env python3
"""FIFO caching"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    class FIFOCache that inherits from BaseCaching and is a caching system
    """
    def __init__(self) -> None:
        super().__init__()
        self.temp_cache = []
    """
    Must assign to the dictionary self.cache_data for value key key
    """
    def put(self, key, item):
        self.temp_cache.append(key)
        if key and item:
            self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded = self.temp_cache.pop(0)
            del self.cache_data[discarded]
            print("DISCARD:{}".format(discarded))
    """
    Must return the value in self.cache_data linked to key
    """
    def get(self, key):
        return self.cache_data.get(key)
