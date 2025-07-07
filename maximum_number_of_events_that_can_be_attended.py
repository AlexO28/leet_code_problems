# You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.
# You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.
# Return the maximum number of events you can attend.
from typing import List
from collections import defaultdict
from heapq import heappush, heappop
from math import inf


class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        if len(events) == 1:
            return 1
        event_dict = defaultdict(list)
        earliest_start = inf
        latest_end = 0
        for start, end in events:
            event_dict[start].append(end)
            earliest_start = min(earliest_start, start)
            latest_end = max(latest_end, end)
        min_heap = []
        res = 0
        for day in range(earliest_start, latest_end + 1):
            while min_heap and min_heap[0] < day:
                heappop(min_heap)
            for end in event_dict[day]:
                heappush(min_heap, end)
            if min_heap:
                res += 1
                heappop(min_heap)
        return res
