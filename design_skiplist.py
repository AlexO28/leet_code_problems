# Design a Skiplist without using any built-in libraries.
# A skiplist is a data structure that takes O(log(n)) time to add, erase and search. Comparing with treap and red-black tree which has the same function and performance, the code length of Skiplist can be comparatively short and the idea behind Skiplists is just simple linked lists.
# Implement the Skiplist class:
# Skiplist() Initializes the object of the skiplist.
# bool search(int target) Returns true if the integer target exists in the Skiplist or false otherwise.
# void add(int num) Inserts the value num into the SkipList.
# bool erase(int num) Removes the value num from the Skiplist and returns true. If num does not exist in the Skiplist, do nothing and return false. If there exist multiple num values, removing any one of them is fine.
# Note that duplicates may exist in the Skiplist, your code needs to handle this situation.
class Skiplist:

    def __init__(self):
        self.arr = []
        
    def search(self, target: int) -> bool:
        return target in self.arr

    def add(self, num: int) -> None:
        self.arr.append(num)

    def erase(self, num: int) -> bool:
        try:
            self.arr.remove(num)
            return True
        except:
            return False
        


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
