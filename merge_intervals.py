# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        results = []
        for interval in intervals:
            if interval[0] <= end:
                end = max(interval[1], end)
            else:
                results.append([start, end])
                start = interval[0]
                end = interval[1]
        results.append([start, end])
        return results
