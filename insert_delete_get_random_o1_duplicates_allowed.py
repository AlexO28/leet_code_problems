# RandomizedCollection is a data structure that contains a collection of numbers, possibly duplicates (i.e., a multiset). It should support inserting and removing specific elements and also reporting a random element.
# Implement the RandomizedCollection class:
# RandomizedCollection() Initializes the empty RandomizedCollection object.
# bool insert(int val) Inserts an item val into the multiset, even if the item is already present. Returns true if the item is not present, false otherwise.
# bool remove(int val) Removes an item val from the multiset if present. Returns true if the item is present, false otherwise. Note that if val has multiple occurrences in the multiset, we only remove one of them.
# int getRandom() Returns a random element from the current multiset of elements. The probability of each element being returned is linearly related to the number of the same values the multiset contains.

import random

class RandomizedCollection:

    def __init__(self):
        self.arr = []

    def insert(self, val: int) -> bool:
        check = (val not in self.arr)
        self.arr.append(val)
        return check

    def remove(self, val: int) -> bool:
        check = (val in self.arr)
        if check:
            self.arr.remove(val)
        return check

    def getRandom(self) -> int:
        return self.arr[random.randint(0, len(self.arr)-1)]
