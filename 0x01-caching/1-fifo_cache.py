#!/usr/bin/env python3
"""
This script implements a class FIFOCache that inherits
from BaseCaching and is a caching system.
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    This class uses a FIFO algorithm cache policy
    """

    def __init__(self):
        """calling the parent's class init method
        to initialize self.cache_data and MAX_ITEMS
        """
        super().__init__()

    def put(self, key, item):
        """This method assigns to the dictionary self.cache_data
        the item value for the key.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # A FIFO algorithm to discard the first item in the cache
            # Finding the oldest item by using the order of keys
            first_item = next(iter(self.cache_data))
            # Deleting the first item in self.cache_data and printing it
            del self.cache_data[first_item]
            print("DISCARD: {}".format(first_item))

    def get(self, key):
        """This method returns the value in self.cache_data
        linked to key
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
