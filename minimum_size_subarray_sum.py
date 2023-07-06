# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
from bisect import bisect_left


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cumsum = [0]
        for num in nums:
            cumsum.append(num + cumsum[-1])
        res = len(nums) + 1
        counter = 0
        for num in cumsum:
            j = bisect_left(cumsum, num + target)
            if j != len(nums) + 1:
                res = min(res, j - counter)
            counter += 1
        if res == len(nums) + 1:
            return 0
        else:
            return res
