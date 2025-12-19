# Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.
# A subarray of an array is a consecutive sequence of zero or more values taken out of that array.
# Return the maximum length of a subarray with positive product.
from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        zeros = [-1]
        for j in range(len(nums)):
            if nums[j] == 0:
                zeros.append(j)
        zeros.append(len(nums))
        max_len = 0
        for j in range(len(zeros) - 1):
            start = zeros[j]
            end = zeros[j + 1]
            if end == start + 1:
                continue
            negatives = []
            for i in range(start + 1, end):
                if nums[i] < 0:
                    negatives.append(i)
            if len(negatives) % 2 == 0:
                max_len = max(max_len, end - start - 1)
            else:
                max_len = max(max_len, end - negatives[0] - 1, negatives[-1] - start - 1)
        return max_len
