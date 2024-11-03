# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to the rightmost position.
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)-1):
            if i == 0:
                new_s = s
            else:
                new_s = s[i:] + s[:i]
            if new_s == goal:
                return True
        return False
