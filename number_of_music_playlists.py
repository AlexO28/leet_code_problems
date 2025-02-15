# Your music player contains n different songs. You want to listen to goal songs (not necessarily different) during your trip. To avoid boredom, you will create a playlist so that:
# Every song is played at least once.
# A song can only be played again only if k other songs have been played.
# Given n, goal, and k, return the number of possible playlists that you can create. Since the answer can be very large, return it modulo 109 + 7.
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0]*(n+1) for i in range(goal + 1)]
        dp[0][0] = 1
        for i in range(1, goal+1):
            for j in range(1, n+1):
                if j > k:
                    dp[i][j] = (dp[i-1][j-1]*(n-j+1) + dp[i-1][j]*(j-k)) % MOD
                else:
                    dp[i][j] = dp[i-1][j-1]*(n-j+1) % MOD
        return dp[goal][n]
