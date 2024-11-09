# You are given a string s of length n where s[i] is either:
# 'D' means decreasing, or
# 'I' means increasing.
# A permutation perm of n + 1 integers of all the integers in the range [0, n] is called a valid permutation if for all valid i:
# If s[i] == 'D', then perm[i] > perm[i + 1], and
# If s[i] == 'I', then perm[i] < perm[i + 1].
# Return the number of valid permutations perm. Since the answer may be large, return it modulo 109 + 7.
class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        dp = [1] + [0]*(len(s))
        for j in range(len(s)):
            pre = 0
            new_dp = [0]*(len(s) + 1)
            if s[j] == "D":
                for i in range(j+1, -1, -1):
                    pre = (pre + dp[i]) % MOD
                    new_dp[i] = pre
            else:
                for i in range(j+2):
                    new_dp[i] = pre
                    pre = (pre + dp[i]) % MOD
            dp = new_dp
        return sum(dp) % MOD
