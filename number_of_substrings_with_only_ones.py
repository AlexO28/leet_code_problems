# Given a binary string s, return the number of substrings with all characters 1's. Since the answer may be too large, return it modulo 109 + 7.
class Solution:
    def numSub(self, s: str) -> int:
        s = list(s)
        num_elements = 0
        res = 0
        MOD = 10**9 + 7
        for elem in s:
            if elem == "1":
                num_elements += 1
            else:
                res = (res + (num_elements + 1) * num_elements // 2) % MOD
                num_elements = 0
        if num_elements > 0:
            return (res + (num_elements + 1) * num_elements // 2) % MOD
        else:
            return res
