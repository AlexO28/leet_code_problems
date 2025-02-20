# There is a 2D grid of size n x n where each cell of this grid has a lamp that is initially turned off.
# You are given a 2D array of lamp positions lamps, where lamps[i] = [rowi, coli] indicates that the lamp at grid[rowi][coli] is turned on. Even if the same lamp is listed more than once, it is turned on.
# When a lamp is turned on, it illuminates its cell and all other cells in the same row, column, or diagonal.
# You are also given another 2D array queries, where queries[j] = [rowj, colj]. For the jth query, determine whether grid[rowj][colj] is illuminated or not. After answering the jth query, turn off the lamp at grid[rowj][colj] and its 8 adjacent lamps if they exist. A lamp is adjacent if its cell shares either a side or corner with grid[rowj][colj].
# Return an array of integers ans, where ans[j] should be 1 if the cell in the jth query was illuminated, or 0 if the lamp was not.
from collections import Counter
from typing import List


class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        lamp_positions = {(i, j) for i, j in lamps}
        row_count = Counter()
        col_count = Counter()
        diag1_count = Counter()
        diag2_count = Counter()
        for lamp in lamp_positions:
            row_count[lamp[0]] += 1
            col_count[lamp[1]] += 1
            diag1_count[lamp[0]-lamp[1]] += 1
            diag2_count[lamp[0]+lamp[1]] += 1
        res = [0]*(len(queries))
        for index in range(len(queries)):
            i = queries[index][0]
            j = queries[index][1]
            if row_count[i] or col_count[j] or diag1_count[i-j] or diag2_count[i+j]:
                res[index] = 1
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    if (x, y) in lamp_positions:
                        lamp_positions.remove((x, y))
                        row_count[x] -= 1
                        col_count[y] -= 1
                        diag1_count[x-y] -= 1
                        diag2_count[x+y] -= 1
        return res
