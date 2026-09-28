# You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].
# Implement the SmallestInfiniteSet class:
# SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
# int popSmallest() Removes and returns the smallest integer contained in the infinite set.
# void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.
class SmallestInfiniteSet:

    def __init__(self):
        self.visited = set()
        self.smallest = 1

    def popSmallest(self) -> int:
        res = self.smallest
        while True:
           self.smallest += 1
           if self.smallest not in self.visited:
               break
        self.visited.add(res)
        return res

    def addBack(self, num: int) -> None:
        if num in self.visited:
            self.visited.remove(num)
            self.smallest = min(num, self.smallest)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
