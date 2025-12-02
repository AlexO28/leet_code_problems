# You are given a 2D integer array points, where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.
# A horizontal trapezoid is a convex quadrilateral with at least one pair of horizontal sides (i.e. parallel to the x-axis). Two lines are parallel if and only if they have the same slope.
# Return the number of unique horizontal trapezoids that can be formed by choosing any four distinct points from points.
# Since the answer may be very large, return it modulo 109 + 7.
from collections import Counter
from typing import List


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod = 10**9 + 7
        cnt = Counter(p[1] for p in points)
        ans = 0
        s = 0
        for v in cnt.values():
            t = v * (v - 1) // 2
            ans = (ans + s * t) % mod
            s += t
        return ans
