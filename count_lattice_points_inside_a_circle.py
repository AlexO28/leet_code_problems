# Given a 2D integer array circles where circles[i] = [xi, yi, ri] represents the center (xi, yi) and radius ri of the ith circle drawn on a grid, return the number of lattice points that are present inside at least one circle.
# Note:
# A lattice point is a point with integer coordinates.
# Points that lie on the circumference of a circle are also considered to be inside it.
from typing import List


class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        visited = set()
        for circle in circles:
            rad2 = circle[2] ** 2
            for x in range(circle[0] - circle[2], circle[0] + circle[2] + 1):
                for y in range(circle[1] - circle[2], circle[1] + circle[2] + 1):
                    point = str(x) + "_" + str(y)
                    if point not in visited:
                        if (x - circle[0]) ** 2 + (y - circle[1]) ** 2 <= rad2:
                            visited.add(point)
        return len(visited)
