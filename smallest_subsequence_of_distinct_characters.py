# Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        if len(s) == 1:
            return s
        last = {}
        for j in range(len(s)):
            last[s[j]] = j
        stack = []
        visited = set()
        for j in range(len(s)):
            if s[j] not in visited:
                while stack and stack[-1] > s[j] and last[stack[-1]] > j:
                    visited.remove(stack.pop())
                stack.append(s[j])
                visited.add(s[j])
        return ''.join(stack)
