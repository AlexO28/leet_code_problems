# You are given a 0-indexed integer array nums of length n.
# The average difference of the index i is the absolute difference between the average of the first i + 1 elements of nums and the average of the last n - i - 1 elements. Both averages should be rounded down to the nearest integer.
# Return the index with the minimum average difference. If there are multiple such indices, return the smallest one.
# Note:
# The absolute difference of two numbers is the absolute value of their difference.
# The average of n elements is the sum of the n elements divided (integer division) by n.
# The average of 0 elements is considered to be 0.
from math import inf


class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        prefix_sums = []
        summa = 0
        ind = -1
        diff = inf
        for num in nums:
            summa += num
            prefix_sums.append(summa)
        for i in range(len(nums)):
            val = abs(
                int(prefix_sums[i] / (i + 1))
                - int((summa - prefix_sums[i]) / (len(nums) - i - 1 - 0.000001))
            )
            if diff > val:
                diff = val
                ind = i
        return ind
