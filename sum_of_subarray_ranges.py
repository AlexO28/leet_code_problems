# You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.
# Return the sum of all subarray ranges of nums.
# A subarray is a contiguous non-empty sequence of elements within an array.
from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        summa = 0
        for i in range(len(nums)-1):
            min_val = nums[i]
            max_val = nums[i]
            for j in range(i+1, len(nums)):
                min_val = min(min_val, nums[j])
                max_val = max(max_val, nums[j])
                summa += max_val - min_val
        return summa
