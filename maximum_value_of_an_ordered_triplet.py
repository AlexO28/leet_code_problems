# You are given a 0-indexed integer array nums.
# Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.
# The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].
from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        prefix_max = []
        cur_max = nums[0]
        for i in range(len(nums)):
            cur_max = max(cur_max, nums[i])
            prefix_max.append(cur_max)
        suffix_max = []
        cur_max = nums[-1]
        for i in range(len(nums)-1, -1, -1):
            cur_max = max(cur_max, nums[i])
            suffix_max.append(cur_max)
        suffix_max = suffix_max[::-1]
        max_val = 0
        for j in range(1, len(nums)-1):
            max_val = max(max_val, (prefix_max[j-1] - nums[j]) * suffix_max[j+1])
        return max_val
