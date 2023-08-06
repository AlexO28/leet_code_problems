# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
# Implement the LRUCache class:
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.


from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys_and_values = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.keys_and_values:
            return -1
        self.keys_and_values.move_to_end(key)
        return self.keys_and_values[key]

    def put(self, key: int, value: int) -> None:
        if key not in self.keys_and_values:
            if len(self.keys_and_values) == self.capacity:
                self.keys_and_values.popitem(False)
        self.keys_and_values[key] = value
        self.keys_and_values.move_to_end(key)
