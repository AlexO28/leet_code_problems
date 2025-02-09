# You are given a 0-indexed integer array nums. A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].
# Return the total number of bad pairs in nums.
from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        num_dict = {}
        for j in range(len(nums)):
            val = nums[j] - j
            if val in num_dict:
                num_dict[val] += 1
            else:
                num_dict[val] = 1
        return int((len(nums)*(len(nums)-1) - sum(val*(val-1) for val in num_dict.values() if val >= 2))/2)
