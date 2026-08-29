# You have an array of floating point numbers averages which is initially empty. You are given an array nums of n integers where n is even.
# You repeat the following procedure n / 2 times:
# Remove the smallest element, minElement, and the largest element maxElement, from nums.
# Add (minElement + maxElement) / 2 to averages.
# Return the minimum element in averages.
from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        start = 0
        end = len(nums) - 1
        averages = []
        for j in range(len(nums) // 2):
            averages.append((nums[start] + nums[end]) / 2)
            start += 1
            end -= 1
        return min(averages)
