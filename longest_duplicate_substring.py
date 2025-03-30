# Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.
# Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        left = 0
        right = len(s)
        res = ""
        while left < right:
            mid = (left + right + 1) // 2
            cur_dep = self.has_duplicate(s, mid)
            if len(cur_dep) > len(res):
                res = cur_dep
            if len(cur_dep) > 0:
                left = mid
            else:
                right = mid - 1
        return res


    def has_duplicate(self, s, cur_len):
        seen = set()
        for i in range(len(s) - cur_len + 1):
            substring = s[i: (i + cur_len)]
            if substring in seen:
                return substring
            else:
                seen.add(substring)
        return ""
