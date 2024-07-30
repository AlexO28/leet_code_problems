# You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.
# Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.
# In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.
class Solution:
    def numTilings(self, n: int) -> int:
        if n < 3:
            return n
        MOD = 1e9 + 7
        dp = [[0] * 3 for i in range(n + 1)]
        dp[0][0] = 1
        dp[1][0] = 1
        dp[1][1] = 1
        dp[1][2] = 1
        for i in range(2, n+1):
            dp[i][0] = (dp[i-1][0] + dp[i-2][0] + dp[i-2][1] + dp[i-2][2]) % MOD
            dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % MOD
            dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % MOD
        return int(dp[n][0])
