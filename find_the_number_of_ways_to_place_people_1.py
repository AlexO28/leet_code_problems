# You are given a 2D array points of size n x 2 representing integer coordinates of some points on a 2D plane, where points[i] = [xi, yi].
# Count the number of pairs of points (A, B), where
# A is on the upper left side of B, and
# there are no other points in the rectangle (or line) they make (including the border).
# Return the count.
from typing import List


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points)):
            for j in range(len(points)):
                if j != i:
                    if (
                        (points[j][0] >= points[i][0])
                        and (points[j][1] <= points[i][1])
                        and (points[i] != points[j])
                    ):
                        check = True
                        for k in range(len(points)):
                            if (k != i) and (k != j):
                                if (points[i][0] <= points[k][0] <= points[j][0]) and (
                                    points[j][1] <= points[k][1] <= points[i][1]
                                ):
                                    check = False
                                    break
                        if check:
                            res += 1
        return res
