# You are given an integer array nums. You can choose exactly one index (0-indexed) and remove the element. Notice that the index of the elements may change after the removal.
# An array is fair if the sum of the odd-indexed values equals the sum of the even-indexed values.
# Return the number of indices that you could choose such that after the removal, nums is fair.
from typing import List


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        s1 = 0
        s2 = 0
        for j in range(len(nums)):
            if j % 2 == 0:
                s1 += nums[j]
            else:
                s2 += nums[j]
        ans = 0
        t1 = 0
        t2 = 0
        for i, v in enumerate(nums):
            if i % 2 == 0:
                ans += t2 + s1 - t1 - v == t1 + s2 - t2
                t1 += v
            else:
                ans += t2 + s1 - t1 == t1 + s2 - t2 - v
                t2 += v
        return ans
