# Write a function that reverses a string. The input string is given as an array of characters s.


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) > 1:
            s_copy = s[::-1]
            for j in range(len(s)):
                s[j] = s_copy[j]
