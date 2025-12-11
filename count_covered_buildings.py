# You are given a positive integer n, representing an n x n city. You are also given a 2D grid buildings, where buildings[i] = [x, y] denotes a unique building located at coordinates [x, y].
# A building is covered if there is at least one building in all four directions: left, right, above, and below.
# Return the number of covered buildings.
from typing import List


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        group_x = {}
        group_y = {}
        for x, y in buildings:
            if x in group_x:
                group_x[x].append(y)
            else:
                group_x[x] = [y]
            if y in group_y:
                group_y[y].append(x)
            else:
                group_y[y] = [x]
        covered_by_y = []
        for x in group_x:
            group_x[x].sort()
            if len(group_x[x]) > 2:
                for y in group_x[x][1:(-1)]:
                    covered_by_y.append(str(x) + ":" + str(y))
        covered_by_x = []
        for y in group_y:
            group_y[y].sort()
            if len(group_y[y]) > 2:
                for x in group_y[y][1:(-1)]:
                    covered_by_x.append(str(x) + ":" + str(y))
        covered_by_x = set(covered_by_x)
        covered_by_y = set(covered_by_y)
        return len(covered_by_x & covered_by_y)
