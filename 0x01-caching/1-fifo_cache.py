#!/usr/bin/env python3
"""Create a class FIFOCache that inherits from
BaseCaching and is a caching system:
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """An implementation of FIFO(First In Fisrt Out) Cache
    """

    def __init__(self):
        """Instantiation method, sets instance attributes
        """
        super().__init__()

    def put(self, key, item):
        """
        add an item in the cache
        """
        if key is None or item is None:
            pass
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                first_key = next(iter(self.cache_data.keys()))
                del self.cache_data[first_key]
                print("DISCARD: {}". format(first_key))

            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to a key
        """
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
