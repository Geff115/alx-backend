#!/usr/bin/env python3
"""
This script implements a class LRUCache that inherits
from BaseCaching and is a caching system.
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    This class uses a LRU algorithm
    cache policy
    """

    def __init__(self):
        """Calling the parent's class init method to
        initialize self.cache_data and MAX_ITEMS
        """
        super().__init__()
        self.track_recent = []

    def put(self, key, item):
        """This method assigns to the dictionary self.cache_data
        the item value for the key.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if key in self.track_recent:
            self.track_recent.remove(key)
        # Appending the key to recent usage list
        self.track_recent.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            recent_item = self.track_recent.pop(0)
            if recent_item in self.cache_data:
                del self.cache_data[recent_item]
                print("DISCARD: {}".format(recent_item))

    def get(self, key):
        """This method returns the value in
        self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        if key in self.cache_data:
            self.track_recent.remove(key)
            self.track_recent.append(key)
            return self.cache_data[key]
