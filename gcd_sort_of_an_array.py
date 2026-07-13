# You are given an integer array nums, and you can perform the following operation any number of times on nums:
# Swap the positions of two elements nums[i] and nums[j] if gcd(nums[i], nums[j]) > 1 where gcd(nums[i], nums[j]) is the greatest common divisor of nums[i] and nums[j].
# Return true if it is possible to sort nums in non-decreasing order using the above swap method, or false otherwise.
from typing import List
from collections import defaultdict


class Solution:
    def gcdSort(self, nums: List[int]) -> bool:
        self.p = list(range(100001))
        f = defaultdict(list)
        mx = max(nums)
        for i in range(2, mx + 1):
            if f[i]:
                continue
            for j in range(i, mx + 1, i):
                f[j].append(i)
        for i in nums:
            for j in f[i]:
                self.p[self.find(i)] = self.find(j)
        s = sorted(nums)
        for i, num in enumerate(nums):
            if s[i] != num and self.find(num) != self.find(s[i]):
                return False
        return True      

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
