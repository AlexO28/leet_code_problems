# The hash of a 0-indexed string s of length k, given integers p and m, is computed using the following function:
# hash(s, p, m) = (val(s[0]) * p0 + val(s[1]) * p1 + ... + val(s[k-1]) * pk-1) mod m.
# Where val(s[i]) represents the index of s[i] in the alphabet from val('a') = 1 to val('z') = 26.
# You are given a string s and the integers power, modulo, k, and hashValue. Return sub, the first substring of s of length k such that hash(sub, power, modulo) == hashValue.
# The test cases will be generated such that an answer always exists.
# A substring is a contiguous non-empty sequence of characters within a string.
class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        h = 0
        p = 1
        new_s = [ord(elem) - ord("a") + 1 for elem in s]
        for i in range(len(s) - 1, len(s) - 1 - k, -1):
            h = ((h * power) + new_s[i]) % modulo
            if i != len(s) - k:
                p = p * power % modulo
        j = len(s) - k
        for i in range(len(s) - 1 - k, -1, -1):
            h = ((h - new_s[i + k] * p) * power + new_s[i]) % modulo
            if h == hashValue:
                j = i
        return s[j : j + k]
