# You wrote down many positive integers in a string called num. However, you realized that you forgot to add commas to seperate the different numbers. You remember that the list of integers was non-decreasing and that no integer had leading zeros.
# Return the number of possible lists of integers that you could have written down to get the string num. Since the answer may be large, return it modulo 109 + 7.
class Solution:
    def numberOfCombinations(self, num: str) -> int:
        MOD = 1000000007
        self.num = num
        self.lcp = [[0] * (len(num) + 1) for _ in range(len(num) + 1)]
        for i in range(len(num) - 1, -1, -1):
            for j in range(len(num) - 1, -1, -1):
                if num[i] == num[j]:
                    self.lcp[i][j] = 1 + self.lcp[i + 1][j + 1]
        dp = [[0] * (len(num) + 1) for _ in range(len(num) + 1)]
        dp[0][0] = 1
        for i in range(1, len(num) + 1):
            for j in range(1, i + 1):
                v = 0
                delta = i - j
                delta2 = i - 2 * j
                if num[delta] != "0":
                    if delta2 >= 0 and self.cmp(delta, delta2, j):
                        v = dp[delta][j]
                    else:
                        v = dp[delta][min(j - 1, delta)]
                dp[i][j] = (dp[i][j - 1] + v) % MOD
        return dp[-1][-1]

    def cmp(self, i, j, k):
        return (
            self.lcp[i][j] >= k
            or self.num[i + self.lcp[i][j]] >= self.num[j + self.lcp[i][j]]
        )
