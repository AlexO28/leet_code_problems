# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        newIntervals = []
        detected = False
        start = newInterval[0]
        end = newInterval[1]
        for interval in intervals:
            if interval[1] < newInterval[0]:
                newIntervals.append(interval)
            elif interval[0] > newInterval[1]:
                if not detected:
                    newIntervals.append([start, end])
                    newIntervals.append(interval)
                    detected = True
                else:
                    newIntervals.append(interval)
            elif (newInterval[0] >= interval[0]) and (newInterval[1] >= interval[1]):
                start = min(interval[0], start)
                end = max(newInterval[1], end)
            elif (newInterval[0] >= interval[0]) and (newInterval[1] <= interval[1]):
                start = min(interval[0], start)
                end = max(interval[1], end)
            elif (newInterval[0] <= interval[0]) and (newInterval[1] >= interval[1]):
                start = min(newInterval[0], start)
                end = max(newInterval[1], end)
            elif (newInterval[0] <= interval[0]) and (newInterval[1] <= interval[1]):
                start = min(newInterval[0], start)
                end = max(interval[1], end)
        if not detected:
            newIntervals.append([start, end])
        return newIntervals
