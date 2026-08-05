# You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei. You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.
# Return this maximum sum.
# Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time t, the next event must start at or after t + 1.
import bisect
from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        start_times = [elem[0] for elem in events]
        end_times = [elem[1] for elem in events]
        values = [elem[2] for elem in events]
        max_sum = -1
        max_val = values[-1]
        max_vals = []
        for elem in values[::-1]:
            max_val = max(max_val, elem)
            max_vals.append(max_val)
        max_vals = max_vals[::-1]
        for i in range(len(start_times)):
            if i == len(start_times) - 1:
                max_sum = max(max_sum, values[i])
            else:
                index = bisect.bisect_right(start_times, end_times[i])
                if index < len(values):
                    max_sum = max(max_sum, values[i] + max_vals[index])
                else:
                    max_sum = max(max_sum, values[i])
        return max_sum
