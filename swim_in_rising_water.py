# You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).
# The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.
# Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        self.deltaRow = [-1, 0, 1, 0]
        self.deltaCol = [0, 1, 0, -1]
        low = -1
        high = len(grid) ** 2
        mid = (low + high) // 2
        while low + 1 < high:
            if self.isEndReachable(grid, mid):
                high = mid
            else:
                low = mid
            mid = (low + high) // 2
        return high

    def isEndReachable(self, grid, t):
        if grid[0][0] > t:
            return False
        vis = [[False] * len(grid) for a in range(len(grid))]
        q = [(0, 0)]
        vis[0][0] = True
        while len(q) > 0:
            (curRow, curCol) = q.pop()
            for i in range(4):
                newRow = curRow + self.deltaRow[i]
                newCol = curCol + self.deltaCol[i]
                if (newRow < 0) or (newRow >= len(grid)) or (newCol < 0) or (newCol >= len(grid)):
                    continue
                if vis[newRow][newCol]:
                    continue
                if grid[newRow][newCol] > t:
                    continue
                vis[newRow][newCol] = True
                q.append([newRow, newCol])
        return vis[len(grid) - 1][len(grid) - 1]
