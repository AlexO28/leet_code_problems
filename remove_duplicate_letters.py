# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
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
