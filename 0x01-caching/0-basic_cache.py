#!/usr/bin/env python3
"""
This script creates a caching system named BasicCache
that inherits from BaseCaching.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    This class inherits from BaseCaching, and it doesn't
    have limit.
    """

    def __init__(self):
        """Calling the parent's init method to use self.cache_data()"""
        super().__init__()

    def put(self, key, item):
        """This method assign to the dictionary the item value for the key"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """This method returns the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data:
            return
        value = self.cache_data[key]
        return value
