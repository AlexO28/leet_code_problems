# You are given three integers n, m and k. Consider the following algorithm to find the maximum element of an array of positive integers:
# You should build the array arr which has the following properties:
# arr has exactly n integers.
# 1 <= arr[i] <= m where (0 <= i < n).
# After applying the mentioned algorithm to arr, the value search_cost is equal to k.
# Return the number of ways to build the array arr under the mentioned conditions. As the answer may grow large, the answer must be computed modulo 109 + 7.
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if k == 0:
            return 0
        dp = [[[0] * (m + 1) for i in range(k + 1)] for j in range(n + 1)]
        MOD = 10**9 + 7
        for max_value in range(1, m + 1):
            dp[1][1][max_value] = 1
        for length in range(2, n + 1):
            for search_cost in range(1, min(k + 1, length + 1)):
                for max_value in range(1, m + 1):
                    dp[length][search_cost][max_value] = (
                        dp[length - 1][search_cost][max_value] * max_value
                    ) % MOD
                    for prev_max in range(1, max_value):
                        dp[length][search_cost][max_value] = (
                            dp[length][search_cost][max_value]
                            + dp[length - 1][search_cost - 1][prev_max]
                        ) % MOD
        result = 0
        for max_value in range(1, m + 1):
            result = (result + dp[n][k][max_value]) % MOD
        return result
