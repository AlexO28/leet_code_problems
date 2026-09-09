# There is an n x n 0-indexed grid with some artifacts buried in it. You are given the integer n and a 0-indexed 2D integer array artifacts describing the positions of the rectangular artifacts where artifacts[i] = [r1i, c1i, r2i, c2i] denotes that the ith artifact is buried in the subgrid where:
# (r1i, c1i) is the coordinate of the top-left cell of the ith artifact and
# (r2i, c2i) is the coordinate of the bottom-right cell of the ith artifact.
# You will excavate some cells of the grid and remove all the mud from them. If the cell has a part of an artifact buried underneath, it will be uncovered. If all the parts of an artifact are uncovered, you can extract it.
# Given a 0-indexed 2D integer array dig where dig[i] = [ri, ci] indicates that you will excavate the cell (ri, ci), return the number of artifacts that you can extract.
# The test cases are generated such that:
# No two artifacts overlap.
# Each artifact only covers at most 4 cells.
# The entries of dig are unique.
from typing import List


class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        grid = [[0] * n for i in range(n)]
        for j in range(len(artifacts)):
            ind = j + 1
            for x in range(artifacts[j][0], artifacts[j][2] + 1):
                for y in range(artifacts[j][1], artifacts[j][3] + 1):
                    grid[x][y] = ind
        for x, y in dig:
            grid[x][y] = 0
        numbers = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    numbers.append(grid[i][j])
        return len(artifacts) - len(set(numbers))
