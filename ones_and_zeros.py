# You are given an array of binary strings strs and two integers m and n.
# Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.
# A set x is a subset of a set y if all elements of x are also elements of y.
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        for num in strs:
            total = len(num)
            num_ones = len([elem for elem in num if elem == "1"])
            num_zeros = total - num_ones
            if (num_ones <= n) and (num_zeros <= m):
                for i in range(m, num_zeros-1, -1):
                    for j in range(n, num_ones-1, -1):
                        dp[i][j] = max(dp[i][j], dp[i-num_zeros][j-num_ones]+1)
        return dp[-1][-1]
