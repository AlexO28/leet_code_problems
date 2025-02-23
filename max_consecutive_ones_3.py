# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = -1
        right = -1
        while right < len(nums) - 1:
            right += 1
            if nums[right] == 0:
                k -= 1
            if k < 0:
                left += 1
                if nums[left] == 0:
                    k += 1
        return right - left
