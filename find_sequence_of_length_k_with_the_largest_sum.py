# You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.
# Return any such subsequence as an integer array of length k.
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums_copy = nums.copy()
        nums.sort(reverse=True)
        chosen = nums[:k]
        res = []
        for num in nums_copy:
            if num in chosen:
                res.append(num)
                chosen.remove(num)
                if len(chosen) == 0:
                    break
        return res
