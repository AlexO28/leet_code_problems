# Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.
# The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.
# Return the number of remaining intervals.
from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = list({(interval[0], interval[1]) for interval in intervals})
        if len(intervals) == 1:
            return 1
        res = []
        for i in range(len(intervals)):
            found = False
            for j in range(len(intervals)):
                if i != j:
                    if self.is_covered(intervals[i], intervals[j]):
                        found = True
                        break
            if not found:
                res.append(intervals[i])
        return len(res)

    def is_covered(self, interval_1, interval_2):
        return (interval_2[0] <= interval_1[0]) and (interval_1[1] <= interval_2[1])
