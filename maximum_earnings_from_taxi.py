# There are n points on a road you are driving your taxi on. The n points on the road are labeled from 1 to n in the direction you are going, and you want to drive from point 1 to point n to make money by picking up passengers. You cannot change the direction of the taxi.
# The passengers are represented by a 0-indexed 2D integer array rides, where rides[i] = [starti, endi, tipi] denotes the ith passenger requesting a ride from point starti to point endi who is willing to give a tipi dollar tip.
# For each passenger i you pick up, you earn endi - starti + tipi dollars. You may only drive at most one passenger at a time.
# Given n and rides, return the maximum number of dollars you can earn by picking up the passengers optimally.
# Note: You may drop off a passenger and pick up a different passenger at the same point.
from typing import List
from bisect import bisect_left


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key=lambda x: x[1])
        f = [0] * (len(rides) + 1)
        for i, (start, end, tip) in enumerate(rides, 1):
            j = bisect_left(rides, start + 1, hi=i, key=lambda x: x[1])
            f[i] = max(f[i - 1], f[j] + end - start + tip)
        return f[-1]
