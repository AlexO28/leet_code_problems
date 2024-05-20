# On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).
# Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.
# The knight continues moving until it has made exactly k moves or has moved off the chessboard.
# Return the probability that the knight remains on the board after it has stopped moving.
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dirs = ((1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2))
        dp = [[0] * n for _ in range(n)]
        dp[row][column] = 1.0
        for o in range(k):
            newDp = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for dx, dy in dirs:
                        x = i + dx
                        y = j + dy
                        if 0 <= x < n and 0 <= y < n:
                            newDp[i][j] += dp[x][y]
            dp = newDp
        return sum(map(sum, dp)) / 8**k
