# A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.
# Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) == 1:
            return ""
        max_len = 0
        best_str = ""
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                delta = j + 1 - i
                if delta <= max_len:
                    continue
                s_set = set(list(s[i : (j + 1)]))
                found = False
                for elem in s_set:
                    if (elem.lower() not in s_set) or (elem.upper() not in s_set):
                        found = True
                        break
                if not found:
                    max_len = max(max_len, delta)
                    best_str = s[i : (j + 1)]
        return best_str
