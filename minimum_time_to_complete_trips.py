# You are given an array time where time[i] denotes the time taken by the ith bus to complete one trip.
# Each bus can make multiple trips successively; that is, the next trip can start immediately after completing the current trip. Also, each bus operates independently; that is, the trips of one bus do not influence the trips of any other bus.
# You are also given an integer totalTrips, which denotes the number of trips all buses should make in total. Return the minimum time required for all buses to complete at least totalTrips trips.
from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        self.time = time
        start = 1
        end = totalTrips * min(time)
        while end - start > 1:
            mid = (end + start) // 2
            if self.search(mid) < totalTrips:
                start = mid
            else:
                end = mid
        if end == start:
            return start
        elif self.search(start) >= totalTrips:
            return start
        else:
            return end

    def search(self, time_elapsed):
        res = 0
        for j in range(len(self.time)):
            res += time_elapsed // self.time[j]
        return res
