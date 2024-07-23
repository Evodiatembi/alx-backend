#!/usr/bin/python3
"""Basic Cache implementation Class
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
        """
        A basic cache implementaion class

        """
        def __init__(self):
            """basic cache implementation 
            """
            super().__init__()
            """basic cache implementation
            """
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

