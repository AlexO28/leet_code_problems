# Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.
# Implement the AllOne class:
# AllOne() Initializes the object of the data structure.
# inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
# dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
# getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
# getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
# Note that each function must run in O(1) average time complexity.
class AllOne:

    def __init__(self):
        self.dict = {}
        self.rev_dict = {}        

    def inc(self, key: str) -> None:
        if key in self.dict:
            val = self.dict[key]
            self.dict[key] = val + 1
            self.rev_dict[val].remove(key)
            if len(self.rev_dict[val]) == 0:
                del self.rev_dict[val]
            if val + 1 in self.rev_dict:
                self.rev_dict[val + 1].append(key)
            else:
                self.rev_dict[val + 1] = [key]
        else:
            self.dict[key] = 1
            if 1 in self.rev_dict:
                self.rev_dict[1].append(key)
            else:
                self.rev_dict[1] = [key]

    def dec(self, key: str) -> None:
        val = self.dict[key]
        if val > 1:
            self.dict[key] = val - 1
            self.rev_dict[val].remove(key)
            if len(self.rev_dict[val]) == 0:
                del self.rev_dict[val]
            if val - 1 in self.rev_dict:
                self.rev_dict[val - 1].append(key)
            else:
                self.rev_dict[val - 1] = [key]
        else:
            del self.dict[key]
            self.rev_dict[1].remove(key)
            if len(self.rev_dict[1]) == 0:
                del self.rev_dict[1]

    def getMaxKey(self) -> str:
        if len(self.rev_dict) == 0:
            return ""
        return self.rev_dict[max(self.rev_dict.keys())][0]

    def getMinKey(self) -> str:
        if len(self.rev_dict) == 0:
            return ""
        return self.rev_dict[min(self.rev_dict.keys())][0]

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
