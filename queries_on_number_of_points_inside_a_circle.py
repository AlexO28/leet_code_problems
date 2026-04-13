# You are given an array points where points[i] = [xi, yi] is the coordinates of the ith point on a 2D plane. Multiple points can have the same coordinates.
# You are also given an array queries where queries[j] = [xj, yj, rj] describes a circle centered at (xj, yj) with a radius of rj.
# For each query queries[j], compute the number of points inside the jth circle. Points on the border of the circle are considered inside.
# Return an array answer, where answer[j] is the answer to the jth query.
from typing import List


class Solution:
    def countPoints(
        self, points: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        res = []
        for x, y, r in queries:
            cur_res = 0
            for a, b in points:
                if (a - x) ** 2 + (b - y) ** 2 <= r * r:
                    cur_res += 1
            res.append(cur_res)
        return res
