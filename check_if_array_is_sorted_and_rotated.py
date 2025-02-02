# Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.
# There may be duplicates in the original array.
# Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.
from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        nums_2 = nums.copy()
        nums_2.sort()
        nums.extend(nums)
        for i in range(len(nums_2)):
            found = False
            for j in range(len(nums_2)):
                if nums_2[j] != nums[i+j]:
                    found = True
                    break
            if not found:
                return True
        return False
