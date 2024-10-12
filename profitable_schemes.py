# There is a group of n members, and a list of various crimes they could commit. The ith crime generates a profit[i] and requires group[i] members to participate in it. If a member participates in one crime, that member can't participate in another crime.
# Let's call a profitable scheme any subset of these crimes that generates at least minProfit profit, and the total number of members participating in that subset of crimes is at most n.
# Return the number of schemes that can be chosen. Since the answer may be very large, return it modulo 109 + 7.
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10**9 + 7
        dp = [[[0] * (minProfit + 1) for i in range(n + 1)] for j in range(len(group) + 1)]
        for j in range(n + 1):
            dp[0][j][0] = 1
        for i in range(len(group)):
            for j in range(n+1):
                for k in range(minProfit+1):
                    dp[i+1][j][k] = dp[i][j][k]
                    if j >= group[i]:
                        dp[i+1][j][k] = (dp[i+1][j][k] + dp[i][j-group[i]][max(0, k-profit[i])]) % MOD
        return dp[len(group)][n][minProfit]
