# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
# The distance between two adjacent cells is 1.
from collections import deque
from itertools import pairwise


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        res = [[-1] * (len(mat[0])) for j in range(len(mat))]
        q = deque()
        for i, row in enumerate(mat):
            for j, x in enumerate(row):
                if x == 0:
                    res[i][j] = 0
                    q.append((i, j))
        dirs = (-1, 0, 1, 0, -1)
        while q:
            i, j = q.popleft()
            for a, b in pairwise(dirs):
                x = i + a
                y = j + b
                if 0 <= x < len(mat) and 0 <= y < len(mat[0]) and res[x][y] == -1:
                    res[x][y] = res[i][j] + 1
                    q.append((x, y))
        return res
