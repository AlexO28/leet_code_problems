# Given an integer array instructions, you are asked to create a sorted array from the elements in instructions. You start with an empty container nums. For each element from left to right in instructions, insert it into nums. The cost of each insertion is the minimum of the following:
# The number of elements currently in nums that are strictly less than instructions[i].
# The number of elements currently in nums that are strictly greater than instructions[i].
# For example, if inserting element 3 into nums = [1,2,3,5], the cost of insertion is min(2, 1) (elements 1 and 2 are less than 3, element 5 is greater than 3) and nums will become [1,2,3,3,5].
# Return the total cost to insert all elements from instructions into nums. Since the answer may be large, return it modulo 109 + 7
from typing import List


class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        m = max(instructions)
        tree = BinaryIndexedTree(m)
        ans = 0
        mod = 1000000007
        for i, x in enumerate(instructions):
            cost = min(tree.query(x - 1), i - tree.query(x))
            ans += cost
            tree.update(x, 1)
        return ans % mod


class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.c = [0] * (n + 1)

    def update(self, x: int, v: int):
        while x <= self.n:
            self.c[x] += v
            x += x & -x

    def query(self, x: int) -> int:
        s = 0
        while x:
            s += self.c[x]
            x -= x & -x
        return s
