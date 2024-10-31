#!/usr/bin/env python3
"""
This script implements a class LFUCache that inherits
from BaseCaching and is a caching system.
"""

from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """
    This class implements a MRU algorithm
    cache policy
    """

    def __init__(self):
        """Calling the parent's class init method
        to initialize self.cache_data and MAX_ITEMS
        """
        super().__init__()
        # Maps frequency to a list of keys with that frequency
        self.freq = defaultdict(list)
        # Maps each key to its current frequency
        self.key_freq = {}
        # Tracks the minimum frequency in the cache
        self.min_freq = 0

    def put(self, key, item):
        """This method assigns to the dictionary self.cache_data
        the item value for the key.
        """
        if key is None or item is None:
            return

        # If key exists, update the value and frequency
        if key in self.cache_data:
            self.cache_data[key] = item
            self._update_frequency(key)
        else:
            # If the cache is full, evict the least frequently used item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                key_to_evict = self.freq[self.min_freq].pop(0)
                del self.cache_data[key_to_evict]
                del self.key_freq[key_to_evict]
                print("DISCARD:", key_to_evict)

                # Clean up if there are no keys with the min_freq anymore
                if not self.freq[self.min_freq]:
                    del self.freq[self.min_freq]

            # Add new key with frequency 1
            self.cache_data[key] = item
            self.key_freq[key] = 1
            self.freq[1].append(key)
            self.min_freq = 1  # Reset min_freq to 1 for the new item

    def get(self, key):
        """This method returns the value of self.cache_data
        link to key.
        """
        if key is None or key not in self.cache_data:
            return None

        # Update the frequency of the key
        self._update_frequency(key)
        return self.cache_data[key]

    def _update_frequency(self, key):
        """Helper function to update the frequency of an accessed key"""
        freq = self.key_freq[key]

        # Remove the key from the current frequency list
        self.freq[freq].remove(key)

        # Clean up if the current frequency list is empty
        if not self.freq[freq]:
            del self.freq[freq]
            # Update min_freq if this was the smallest frequency
            if freq == self.min_freq:
                self.min_freq += 1

        # Increment key's frequency and add it to the new frequency list
        new_freq = freq + 1
        self.key_freq[key] = new_freq
        self.freq[new_freq].append(key)
