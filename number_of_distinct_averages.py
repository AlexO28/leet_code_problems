# You are given a 0-indexed integer array nums of even length.
# As long as nums is not empty, you must repetitively:
# Find the minimum number in nums and remove it.
# Find the maximum number in nums and remove it.
# Calculate the average of the two removed numbers.
# The average of two numbers a and b is (a + b) / 2.
# Return the number of distinct averages calculated using the above process.
# Note that when there is a tie for a minimum or maximum number, any can be removed.
from typing import List


class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        averages = []
        while len(nums) > 1:
            num1 = nums.pop(0)
            num2 = nums.pop(-1)
            averages.append((num1 + num2) / 2)
        if len(nums) == 1:
            averages.append(nums[0])
        return len(set(averages))
