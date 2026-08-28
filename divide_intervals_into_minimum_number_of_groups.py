# You are given a 2D integer array intervals where intervals[i] = [lefti, righti] represents the inclusive interval [lefti, righti].
# You have to divide the intervals into one or more groups such that each interval is in exactly one group, and no two intervals that are in the same group intersect each other.
# Return the minimum number of groups you need to make.
# Two intervals intersect if there is at least one common number between them. For example, the intervals [1, 5] and [5, 8] intersect.
from heapq import heappop, heappush
from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 1
        intervals.sort()
        q = []
        for left, right in intervals:
            if q and q[0] < left:
                heappop(q)
            heappush(q, right)
        return len(q)
