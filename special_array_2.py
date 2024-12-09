# An array is considered special if every pair of its adjacent elements contains two numbers with different parity.
# You are given an array of integer nums and a 2D integer matrix queries, where for queries[i] = [fromi, toi] your task is to check that 
# subarray
#  nums[fromi..toi] is special or not.
# Return an array of booleans answer such that answer[i] is true if nums[fromi..toi] is special.
from bisect import bisect_left
from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        if len(nums) == 1:
            return [True]*(len(queries))
        indices = []
        ends = []
        starts = []
        start = 0
        for j in range(1, len(nums)):
            if nums[j] % 2 == nums[j-1] % 2:
                starts.append(start)
                ends.append(j)
                start = j
        starts.append(start)
        ends.append(len(nums))
        if len(indices) == 1:
            return [True]*(len(queries))
        res = []
        for start, end in queries:
            pos = bisect_left(ends, start)
            if ends[pos] == start:
                pos += 1
            a = starts[pos]
            b = ends[pos]
            if ((a <= start) and (start < b)) and (end >= b):
                res.append(False)
            else:
                res.append(True)
        return res
