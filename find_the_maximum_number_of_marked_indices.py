# You are given a 0-indexed integer array nums.
# Initially, all of the indices are unmarked. You are allowed to make this operation any number of times:
# Pick two different unmarked indices i and j such that 2 * nums[i] <= nums[j], then mark i and j.
# Return the maximum possible number of marked indices in nums using the above operation any number of times.
from typing import List


class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return 0
        nums.sort()
        i = 0
        mid = (len(nums) + 1) // 2
        for x in nums[mid:]:
            if nums[i] * 2 <= x:
                i += 1
        return i * 2
