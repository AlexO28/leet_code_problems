# Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) <= k:
            return False
        else:
            all_substrings = set()
            all_substrings.add(s[:k])
            for j in range(1, len(s) - k + 1):
                all_substrings.add(s[j : (j + k)])
            return len(all_substrings) == 2**k
