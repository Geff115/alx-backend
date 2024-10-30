#!/usr/bin/env python3
"""
This script implements a MRUCache class that inherits
from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    This class implements a MRU algorithm
    cache policy
    """

    def __init__(self):
        """Calling the parent's class init method
        to initialize self.cache_data and MAX_ITEMS
        """
        super().__init__()
        self.track_records = []

    def put(self, key, item):
        """
        This method assigns to the dictionary self.cache_data the
        item value for the key.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if key in self.track_records:
            self.track_records.remove(key)
        self.track_records.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            most_recent_item = self.track_records.pop(-2)
            del self.cache_data[most_recent_item]
            print("DISCARD: {}".format(most_recent_item))

    def get(self, key):
        """
        This method returns the value in self.cache_data
        linked to key.
        """
        if key is None or key not in self.cache_data:
            return None

        if key in self.cache_data:
            self.track_records.remove(key)
            self.track_records.append(key)
            return self.cache_data[key]
