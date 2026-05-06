# You are given a floating-point number hour, representing the amount of time you have to reach the office. To commute to the office, you must take n trains in sequential order. You are also given an integer array dist of length n, where dist[i] describes the distance (in kilometers) of the ith train ride.
# Each train can only depart at an integer hour, so you may need to wait in between each train ride.
# For example, if the 1st train ride takes 1.5 hours, you must wait for an additional 0.5 hours before you can depart on the 2nd train ride at the 2 hour mark.
# Return the minimum positive integer speed (in kilometers per hour) that all the trains must travel at for you to reach the office on time, or -1 if it is impossible to be on time.
# Tests are generated such that the answer will not exceed 107 and hour will have at most two digits after the decimal point.
import math
from typing import List
from bisect import bisect_left


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) > math.ceil(hour):
            return -1
        self.dist = dist
        self.hour = hour
        ans = bisect_left(range(1, 10000001), True, key=self.check) + 1
        if ans == 10000001:
            return -1
        else:
            return ans

    def check(self, v):
        s = 0
        for i, d in enumerate(self.dist):
            t = d / v
            if i == len(self.dist) - 1:
                s += t
            else:
                s += math.ceil(t)
        return s <= self.hour
