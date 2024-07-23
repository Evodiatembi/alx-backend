#!/usr/bin/python3
"""Basic Cache implementation Class
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
        """
        A basic cache implementaion class

        Attributes:
            MAX_ITEMS: number of items that can be store in the cache
        """
        def __init__(self):
            """_summary_
            """
            super().__init__()
        def put(self, key, item):
            """ Add an item in the cache
            """
            if key is not None and item is not None:
                self.cache_data[key] = item

        def get(self, key):
            """ Get an item by key
            """
            if key is None or key not in self.cache_data:
               return None
            return self.cache_data[key]

