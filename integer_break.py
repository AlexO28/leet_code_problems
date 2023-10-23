# Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
# Return the maximum product you can get.


class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [1]*(n+1)
        # k --- количество слагаемых
        for k in range(3, n+1):
            # j --- первое число
            for j in range(1, k):
                dp[k] = max(dp[k], j*max(k-j, dp[k-j]))
        return dp[-1]
   
