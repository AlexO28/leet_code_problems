# Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.
# A boomerang is a set of three points that are all distinct and not in a straight line.
from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        dists = []
        dists.append(((points[0][0] - points[1][0]) ** 2 + (points[0][1] - points[1][1]) ** 2) ** 0.5)
        dists.append(((points[2][0] - points[1][0]) ** 2 + (points[2][1] - points[1][1]) ** 2) ** 0.5)
        dists.append(((points[0][0] - points[2][0]) ** 2 + (points[0][1] - points[2][1]) ** 2) ** 0.5)
        dists.sort()
        return round(dists[0] + dists[1], 10) > round(dists[2], 10)
