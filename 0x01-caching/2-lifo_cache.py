#!/usr/bin/env python3
"""
This script implements a class LIFOCache that inherits
from BaseCaching and is a caching system.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """This class uses a LIFO algorithm
    cache policy.
    """

    def __init__(self):
        """Calling the parent's class init method to
        initialize self.cache_data and MAX_ITEMS
        """
        super().__init__()
        self.track_order = []

    def put(self, key, item):
        """This method assigns to the dictionary self.cache_data
        the item value for the key
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.track_order.append(key)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Implementing a LIFO algorithm that removes the last item
            # Removing the last item in the dictionary which is the newest
            last_key = self.track_order[-2]
            self.track_order.remove(last_key)
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))

    def get(self, key):
        """
        This method returns the value in self.cache_data
        linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
