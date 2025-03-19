# You are given a binary array nums.
# You can do the following operation on the array any number of times (possibly zero):
# Choose any 3 consecutive elements from the array and flip all of them.
# Flipping an element means changing its value from 0 to 1, and from 1 to 0.
# Return the minimum number of operations required to make all elements in nums equal to 1. If it is impossible, return -1.
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        min_operations = 0
        i = 0
        while i < len(nums)-2:
            if nums[i] == 0:
                nums[i+1] = self.flip(nums[i+1])
                nums[i+2] = self.flip(nums[i+2])
                min_operations += 1
            i += 1
        if (nums[i] == 0) or (nums[i+1] == 0):
            return -1
        else:
            return min_operations


    def flip(self, num):
        if num == 0:
            return 1
        else:
            return 0
