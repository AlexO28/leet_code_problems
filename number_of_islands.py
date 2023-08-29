# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.


class Solution:
    def check(self, grid, m, n, i, j):
        return 0 <= i < m and 0 <= j < n and grid[i][j] == "1"

    def find(self, p, x):
        if p[x] != x:
            p[x] = self.find(p, p[x])
        return p[x]

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if (m == 1) and (n == 1):
            return int(grid[0][0])
        p = list(range(m * n))
        cur = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    cur += 1
                    for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        if self.check(grid, m, n, i + x, j + y):
                            ind1 = self.find(p, i * n + j)
                            ind2 = self.find(p, (i + x) * n + j + y)
                            if ind1 != ind2:
                                p[ind1] = ind2
                                cur -= 1
        return cur
