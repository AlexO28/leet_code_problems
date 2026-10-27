# You are given an integer array nums and an integer k.
# Find the longest subsequence of nums that meets the following requirements:
# The subsequence is strictly increasing and
# The difference between adjacent elements in the subsequence is at most k.
# Return the length of the longest subsequence that meets the requirements.
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
class Solution:
    def lengthOfLIS(self, nums: list[int], k: int) -> int:
        tree = SegmentTree(max(nums))
        res = 1
        for v in nums:
            t = tree.query(1, v - k, v - 1) + 1
            res = max(res, t)
            tree.modify(1, v, t)
        return res

class SegmentTree:
    def __init__(self, n):
        self.tr = [Node() for _ in range(4 * n)]
        self.build(1, 1, n)

    def build(self, u, l, r):
        self.tr[u].l = l
        self.tr[u].r = r
        if l != r:
            mid = (l + r) >> 1
            uu = u << 1
            self.build(uu, l, mid)
            self.build(uu | 1, mid + 1, r)

    def modify(self, u, x, v):
        if self.tr[u].l == x and self.tr[u].r == x:
            self.tr[u].v = v
        else:
            mid = (self.tr[u].l + self.tr[u].r) >> 1
            if x <= mid:
                self.modify(u << 1, x, v)
            else:
                self.modify(u << 1 | 1, x, v)
            self.pushup(u)

    def pushup(self, u):
        uu = u << 1
        self.tr[u].v = max(self.tr[uu].v, self.tr[uu | 1].v)

    def query(self, u, l, r):
        if self.tr[u].l >= l and self.tr[u].r <= r:
            return self.tr[u].v
        mid = (self.tr[u].l + self.tr[u].r) >> 1
        v = 0
        uu = u << 1
        if l <= mid:
            v = self.query(uu, l, r)
        if r > mid:
            v = max(v, self.query(uu | 1, l, r))
        return v
        
class Node:
    def __init__(self):
        self.l = 0
        self.r = 0
        self.v = 0
