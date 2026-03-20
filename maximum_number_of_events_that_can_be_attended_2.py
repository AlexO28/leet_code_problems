# You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith event starts at startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei. You are also given an integer k which represents the maximum number of events you can attend.
# You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. Note that the end day is inclusive: that is, you cannot attend two events where one of them starts and the other ends on the same day.
# Return the maximum sum of values that you can receive by attending events.
from typing import List
from functools import cache
from bisect import bisect_right


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        self.events = events
        self.events.sort()
        return self.search(0, k)

    @cache
    def search(self, i: int, k: int) -> int:
        if i >= len(self.events):
            return 0
        _, ed, val = self.events[i]
        ans = self.search(i + 1, k)
        if k:
            j = bisect_right(self.events, ed, lo=i + 1, key=lambda x: x[0])
            ans = max(ans, self.search(j, k - 1) + val)
        return ans
