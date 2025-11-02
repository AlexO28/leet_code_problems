# You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.
# A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.
# Return the number of unoccupied cells that are not guarded.
from typing import List


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        cells = [[0] * n for i in range(m)]
        for row, col in guards:
            cells[row][col] = -1
        for row, col in walls:
            cells[row][col] = -1
        for row, col in guards:
            if row > 0:
                for i in range(row - 1, -1, -1):
                    if cells[i][col] >= 0:
                        cells[i][col] = 1
                    else:
                        break
            if row < m - 1:
                for i in range(row + 1, m):
                    if cells[i][col] >= 0:
                        cells[i][col] = 1
                    else:
                        break
            if col > 0:
                for i in range(col - 1, -1, -1):
                    if cells[row][i] >= 0:
                        cells[row][i] = 1
                    else:
                        break
            if col < n - 1:
                for i in range(col + 1, n):
                    if cells[row][i] >= 0:
                        cells[row][i] = 1
                    else:
                        break
        res = 0
        for i in range(m):
            for j in range(n):
                if cells[i][j] == 0:
                    res += 1
        return res
