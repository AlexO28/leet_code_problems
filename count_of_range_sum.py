# Given an integer array nums and two integers lower and upper, return the number of range sums that lie in [lower, upper] inclusive.

import bisect


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        res = 0
        init_vals = [0]*(len(nums) + 1)
        b = [0]*(len(nums) + 2)
        for i in range(len(nums)):
            init_vals[i+1] = init_vals[i] + nums[i]
        sorted_vals = sorted(init_vals)
        for val in init_vals:
            res += self.sumRange(b, bisect.bisect_right(sorted_vals, val-lower)) -\
                self.sumRange(b, bisect.bisect_left(sorted_vals, val-upper))
            b = self.update(b, bisect.bisect_left(sorted_vals, val) + 1, 1)
        return res

    def sumRange(self, b, i):
        res = 0
        while i > 0:
            res += b[i]
            i -= (i & -i)
        return res

    def update(self, b, i, delta):
        while i < len(b):
            b[i] += delta
            i += (i & -i)
        return b
