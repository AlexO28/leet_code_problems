# You are given an m x n binary matrix grid and an integer health.
# You start on the upper-left corner (0, 0) and would like to get to the lower-right corner (m - 1, n - 1).
# You can move up, down, left, or right from one cell to another adjacent cell as long as your health remains positive.
# Cells (i, j) with grid[i][j] = 1 are considered unsafe and reduce your health by 1.
# Return true if you can reach the final cell with a health value of 1 or more, and false otherwise.
from typing import List
from collections import deque
from math import inf


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        queue = deque(["0-0"])
        damage = [[inf] * len(grid[0]) for _ in range(len(grid))]
        damage[0][0] = grid[0][0]
        while queue:
            current_node = queue.popleft()
            i, j = current_node.split("-")
            i = int(i)
            j = int(j)
            for direction in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                next_i = i + direction[0]
                next_j = j + direction[1]
                if (0 <= next_i < len(grid)) and (0 <= next_j < len(grid[0])):
                    next_damage = damage[i][j] + grid[next_i][next_j]
                    if damage[next_i][next_j] > next_damage:
                        damage[next_i][next_j] = next_damage
                        next_node = str(next_i) + "-" + str(next_j)
                        queue.append(next_node)
        return damage[-1][-1] < health
