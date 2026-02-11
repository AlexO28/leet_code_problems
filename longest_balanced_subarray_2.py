# You are given an integer array nums.
# A subarray is called balanced if the number of distinct even numbers in the subarray is equal to the number of distinct odd numbers.
# Return the length of the longest balanced subarray.
from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        self.tr = [Node() for i in range(4 * (len(nums) + 1))]
        self.build(1, 0, len(nums))
        last = {}
        now = 0
        ans = 0
        for i, x in enumerate(nums, start=1):
            if x & 1:
                det = 1
            else:
                det = -1
            if x in last:
                self.modify(1, last[x], len(nums), -det)
                now -= det
            last[x] = i
            self.modify(1, i, len(nums), det)
            now += det
            pos = self.query(1, now)
            ans = max(ans, i - pos)
        return ans

    def build(self, u, l, r):
        self.tr[u].l = l
        self.tr[u].r = r
        self.tr[u].mn = 0
        self.tr[u].mx = 0
        self.tr[u].lazy = 0
        if l == r:
            return
        mid = (l + r) >> 1
        self.build(u << 1, l, mid)
        self.build(u << 1 | 1, mid + 1, r)

    def apply(self, u, v):
        self.tr[u].mn += v
        self.tr[u].mx += v
        self.tr[u].lazy += v

    def pushdown(self, u):
        if self.tr[u].lazy:
            self.apply(u << 1, self.tr[u].lazy)
            self.apply(u << 1 | 1, self.tr[u].lazy)
            self.tr[u].lazy = 0

    def pushup(self, u):
        self.tr[u].mn = min(self.tr[u << 1].mn, self.tr[u << 1 | 1].mn)
        self.tr[u].mx = max(self.tr[u << 1].mx, self.tr[u << 1 | 1].mx)

    def modify(self, u, l, r, v):
        if self.tr[u].l >= l and self.tr[u].r <= r:
            self.apply(u, v)
            return
        self.pushdown(u)
        mid = (self.tr[u].l + self.tr[u].r) >> 1
        if l <= mid:
            self.modify(u << 1, l, r, v)
        if r > mid:
            self.modify(u << 1 | 1, l, r, v)
        self.pushup(u)

    def query(self, u, target):
        if self.tr[u].l == self.tr[u].r:
            return self.tr[u].l
        self.pushdown(u)
        if (self.tr[u << 1].mn <= target) and (target <= self.tr[u << 1].mx):
            return self.query(u << 1, target)
        return self.query(u << 1 | 1, target)


class Node:
    __slots__ = ("l", "r", "mn", "mx", "lazy")

    def __init__(self):
        self.l = self.r = 0
        self.mn = self.mx = 0
        self.lazy = 0
