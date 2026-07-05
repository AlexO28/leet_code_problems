# You are given a binary string binary. A subsequence of binary is considered good if it is not empty and has no leading zeros (with the exception of "0").
# Find the number of unique good subsequences of binary.
# Return the number of unique good subsequences of binary. Since the answer may be very large, return it modulo 109 + 7.
# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        f = 0
        g = 0
        ans = 0
        MOD = 1000000007
        for c in binary:
            if c == "0":
                g = (g + f) % MOD
                ans = 1
            else:
                f = (f + g + 1) % MOD
        return (ans + f + g) % MOD
