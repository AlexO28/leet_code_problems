# You are given an array of points in the X-Y plane points where points[i] = [xi, yi].
# Return the minimum area of any rectangle formed from these points, with sides not necessarily parallel to the X and Y axes. If there is not any such rectangle, return 0.
# Answers within 10-5 of the actual answer will be accepted.
from typing import List
from math import sqrt, inf


class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        if len(points) < 4:
            return 0
        point_set = {(x, y) for x, y in points}      
        min_area = inf
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(len(points)):
                if j != i:
                    x2, y2 = points[j]
                    for k in range(j + 1, len(points)):
                        if k != i:
                            x3, y3 = points[k]
                            x4 = x2 - x1 + x3
                            y4 = y2 - y1 + y3
                            if (x4, y4) in point_set:
                                vector_21 = (x2 - x1, y2 - y1)
                                vector_31 = (x3 - x1, y3 - y1)
                                if vector_21[0] * vector_31[0] + vector_21[1] * vector_31[1] == 0:
                                    width = vector_21[0] ** 2 + vector_21[1] ** 2
                                    height = vector_31[0] ** 2 + vector_31[1] ** 2
                                    min_area = min(min_area, width * height)
        if min_area == inf:
            return 0
        else:
            return sqrt(min_area)
