# Implement the RandomizedSet class:
# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

import random


class RandomizedSet:

    def __init__(self):
        self.arr = []
        

    def insert(self, val: int) -> bool:
        if val in self.arr:
            return False
        else:
            self.arr.append(val)
            return True

    def remove(self, val: int) -> bool:
        try:
            self.arr.remove(val)
            return True
        except:
            return False

    def getRandom(self) -> int:
        return self.arr[random.randint(0, len(self.arr)-1)]        

