# You are given two 0-indexed integer arrays nums1 and nums2, each of size n, and an integer diff. Find the number of pairs (i, j) such that:
# 0 <= i < j <= n - 1 and
# nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff.
# Return the number of pairs that satisfy the conditions.
class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], diff: int) -> int:
        tree = BinaryIndexedTree(100000)
        res = 0
        for a, b in zip(nums1, nums2):
            v = a - b + 40000
            res += tree.query(v + diff)
            tree.update(v, 1)
        return res

class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.c = [0] * (n + 1)

    @staticmethod
    def lowbit(x):
        return x & -x

    def update(self, x, delta):
        while x <= self.n:
            self.c[x] += delta
            x += BinaryIndexedTree.lowbit(x)

    def query(self, x):
        s = 0
        while x:
            s += self.c[x]
            x -= BinaryIndexedTree.lowbit(x)
        return s
        
