# Given an integer array nums, return the number of all the arithmetic subsequences of nums.
# A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.
# A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.
from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        arithmetic_count = [defaultdict(int) for num in nums]
        total_count = 0
        for i in range(len(nums)):
            current_num = nums[i]
            for j in range(i):
                prev_num = nums[j]
                difference = current_num - prev_num
                total_count += arithmetic_count[j][difference]
                arithmetic_count[i][difference] += arithmetic_count[j][difference] + 1
        return total_count
