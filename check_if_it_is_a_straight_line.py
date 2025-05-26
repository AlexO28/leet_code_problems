# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
from typing import List
from math import pow


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        else:
            x1, y1 = coordinates[0]
            x2, y2 = coordinates[1]
            for j in range(len(coordinates)):
                if (coordinates[j][0] - x1) * (y2 - y1) != (coordinates[j][1] - y1) * (x2 - x1):
                    return False
        return True
