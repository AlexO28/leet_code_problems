# You are given an array target that consists of distinct integers and another integer array arr that can have duplicates.
# In one operation, you can insert any integer at any position in arr. For example, if arr = [1,4,1,2], you can add 3 in the middle and make it [1,4,3,1,2]. Note that you can insert the integer at the very beginning or end of the array.
# Return the minimum number of operations needed to make target a subsequence of arr.
# A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the remaining elements' relative order. For example, [2,7,4] is a subsequence of [4,2,3,7,2,1,4] (the underlined elements), while [2,4,2] is not.
from typing import List


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        d = {x: i for i, x in enumerate(target, 1)}
        nums = [d[x] for x in arr if x in d]
        tree = BinaryIndexedTree(len(target))
        ans = 0
        for x in nums:
            v = tree.query(x - 1) + 1
            ans = max(ans, v)
            tree.update(x, v)
        return len(target) - ans


class BinaryIndexedTree:
    __slots__ = "n", "c"

    def __init__(self, n: int):
        self.n = n
        self.c = [0] * (n + 1)

    def update(self, x: int, v: int):
        while x <= self.n:
            self.c[x] = max(self.c[x], v)
            x += x & -x

    def query(self, x: int) -> int:
        res = 0
        while x:
            res = max(res, self.c[x])
            x -= x & -x
        return res
