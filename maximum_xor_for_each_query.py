# You are given a sorted array nums of n non-negative integers and an integer maximumBit. You want to perform the following query n times:
# Find a non-negative integer k < 2maximumBit such that nums[0] XOR nums[1] XOR ... XOR nums[nums.length-1] XOR k is maximized. k is the answer to the ith query.
# Remove the last element from the current array nums.
# Return an array answer, where answer[i] is the answer to the ith query.
from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_val = (2 ** maximumBit) - 1
        res = []
        sumval = None
        for j in range(len(nums)):
            if j == 0:
                sumval = nums[j]
            else:
                sumval ^= nums[j]
            res.append(sumval ^ max_val)
        return res[::-1]
