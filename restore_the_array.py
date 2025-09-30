# A program was supposed to print an array of integers. The program forgot to print whitespaces and the array is printed as a string of digits s and all we know is that all integers in the array were in the range [1, k] and there are no leading zeros in the array.
# Given the string s and the integer k, return the number of the possible arrays that can be printed as s using the mentioned program. Since the answer may be very large, return it modulo 109 + 7.
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (len(s) + 1)
        dp[-1] = 1
        for i in range(len(s) - 1, -1, -1):
            dp[i] = 0
            curr = 0
            for j in range(i, len(s)):
                if curr == 0 and s[i] == "0":
                    break
                curr = 10 * curr + int(s[j])
                if curr > k:
                    break
                dp[i] = (dp[i] + dp[j + 1]) % MOD
        return dp[0]
