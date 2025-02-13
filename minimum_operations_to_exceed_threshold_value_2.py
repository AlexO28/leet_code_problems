# You are given a 0-indexed integer array nums, and an integer k.
# In one operation, you will:
# Take the two smallest integers x and y in nums.
# Remove x and y from nums.
# Add min(x, y) * 2 + max(x, y) anywhere in the array.
# Note that you can only apply the described operation if nums contains at least two elements.
# Return the minimum number of operations needed so that all elements of the array are greater than or equal to k.
from typing import List
from bisect import insort_left


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        number_of_operations = 0
        while len(nums) >= 2:
            if nums[0] >= k:
                return number_of_operations
            else:
                number_of_operations += 1
                num1 = nums.pop(0)
                num2 = nums.pop(0)
                num = min(num1, num2) * 2 + max(num1, num2)
                bisect.insort_left(nums, num)
        return number_of_operations
