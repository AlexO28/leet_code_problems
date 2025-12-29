# We have an array of integers, nums, and an array of requests where requests[i] = [starti, endi]. The ith request asks for the sum of nums[starti] + nums[starti + 1] + ... + nums[endi - 1] + nums[endi]. Both starti and endi are 0-indexed.
# Return the maximum total sum of all requests among all permutations of nums.
# Since the answer may be too large, return it modulo 109 + 7.
from typing import List


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        d = [0] * len(nums)
        for l, r in requests:
            d[l] += 1
            if r + 1 < len(nums):
                d[r + 1] -= 1
        for i in range(1, len(nums)):
            d[i] += d[i - 1]
        nums.sort()
        d.sort()
        return sum(a * b for a, b in zip(nums, d)) % 1000000007
