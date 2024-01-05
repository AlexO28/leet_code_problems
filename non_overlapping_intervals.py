# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0
        intervals.sort(key=lambda interval: interval[1])      
        removed_intervals_count = 0
        end_time = intervals[0][1]      
        for start, end in intervals[1:]:
            if start >= end_time:
                end_time = end
            else:
                removed_intervals_count += 1              
        return removed_intervals_count
