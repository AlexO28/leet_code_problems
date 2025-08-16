# You are given an integer array nums. The value of this array is defined as the sum of |nums[i] - nums[i + 1]| for all 0 <= i < nums.length - 1.
# You are allowed to select any subarray of the given array and reverse it. You can perform this operation only once.
Find maximum possible value of the final array.
from typing import List
from itertools import pairwise
from math import inf


class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        total_difference = sum(abs(x - y) for x, y in pairwise(nums))
        answer = total_difference
        for x, y in pairwise(nums):
            answer = max(answer, total_difference + abs(nums[0] - y) - abs(x - y))
            answer = max(answer, total_difference + abs(nums[-1] - x) - abs(x - y))
        for coef1, coef2 in pairwise((1, -1, -1, 1, 1)):
            max_difference = -inf
            min_difference = inf
            for x, y in pairwise(nums):
                a = coef1 * x + coef2 * y
                abs_difference = abs(x - y)
                max_difference = max(max_difference, a - abs_difference)
                min_difference = min(min_difference, a + abs_difference)
            answer = max(
                answer, total_difference + max(max_difference - min_difference, 0)
            )
        return answer
