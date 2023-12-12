# Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
import math

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_val = -math.inf
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                max_val = max(max_val, (nums[i]-1)*(nums[j]-1))
        return max_val
