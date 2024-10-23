# You are given k identical eggs and you have access to a building with n floors labeled from 1 to n.
# You know that there exists a floor f where 0 <= f <= n such that any egg dropped at a floor higher than f will break, and any egg dropped at or below floor f will not break.
# Each move, you may take an unbroken egg and drop it from any floor x (where 1 <= x <= n). If the egg breaks, you can no longer use it. However, if the egg does not break, you may reuse it in future moves.
# Return the minimum number of moves that you need to determine with certainty what the value of f is.
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[0]*(n+1) for i in range(k+2)]
        m = 0
        while dp[k][m] < n:
            m += 1
            for i in range(1, k+1):
                dp[i][m] = dp[i][m-1] + dp[i-1][m-1] + 1
        return m
