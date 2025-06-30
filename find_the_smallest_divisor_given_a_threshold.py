# Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.
# Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).
# The test cases are generated so that there will be an answer.
from numpy import ceil
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        self.nums = nums
        self.threshold = threshold
        left = 1
        right = max(self.nums) + 1
        check_left = self.check_divisor(left)
        if check_left == 1:
            return left
        while right - left > 1:
            mid = (left + right) // 2
            check_mid = self.check_divisor(mid)
            if check_mid == 0:
                left = mid
            else:
                right = mid
        return right


    def check_divisor(self, divisor):
        summa = 0
        for j in range(len(self.nums)):
            summa += ceil(self.nums[j]/divisor)
            if summa > self.threshold:
                return 0
        return 1
