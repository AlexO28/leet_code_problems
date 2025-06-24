# You are given a 0-indexed integer array nums and two integers key and k. A k-distant index is an index i of nums for which there exists at least one index j such that |i - j| <= k and nums[j] == key.
# Return a list of all k-distant indices sorted in increasing order.
from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = set()
        for i in range(len(nums)):
            if nums[i] == key:
                for j in range(max(i - k, 0), min(i + k + 1, len(nums))):
                    res.add(j)
        res = list(res)
        res.sort()
        return res
