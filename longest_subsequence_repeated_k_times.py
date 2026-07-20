# You are given a string s of length n, and an integer k. You are tasked to find the longest subsequence repeated k times in string s.
# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
# A subsequence seq is repeated k times in the string s if seq * k is a subsequence of s, where seq * k represents a string constructed by concatenating seq k times.
# Return the longest subsequence repeated k times in string s. If multiple such subsequences are found, return the lexicographically largest one. If there is no such subsequence, return an empty string.
from collections import Counter, deque


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        cnt = Counter(s)
        cs = list(set(s))
        cs.sort()
        q = deque([""])
        res = ""
        while q:
            cur = q.popleft()
            for c in cs:
                nxt = cur + c
                if self.check(nxt, k, s):
                    res = nxt
                    q.append(nxt)
        return res

    def check(self, t, k, s):
        i = 0
        for c in s:
            if c == t[i]:
                i += 1
                if i == len(t):
                    k -= 1
                    if k == 0:
                        return True
                    i = 0
        return False
