# You are given an integer array nums and an integer k.
# An integer h is called valid if all values in the array that are strictly greater than h are identical.
# You are allowed to perform the following operation on nums:
# Select an integer h that is valid for the current values in nums.
# For each index i where nums[i] > h, set nums[i] to h.
# Return the minimum number of operations required to make every element in nums equal to k. If it is impossible to make all elements equal to k, return -1
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = list(set(nums))
        nums.sort()
        if nums[0] < k:
            return -1
        elif nums[-1] == k:
            return 0
        else:
            if nums[0] == k:
                return len(nums) - 1
            else:
                return len(nums)
 
