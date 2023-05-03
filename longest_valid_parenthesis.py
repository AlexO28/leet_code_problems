# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        num_open = 0
        num_close = 0
        for symb in s:
            if symb == '(':
                num_open += 1
            elif symb == ')':
                num_close += 1
            if num_open == num_close:
                max_len = max(max_len, num_close + num_open)
            elif num_close > num_open:
                num_open = 0
                num_close = 0
        num_open = 0
        num_close = 0
        for symb in s[::-1]:
            if symb == '(':
                num_open += 1
            elif symb == ')':
                num_close += 1
            if num_open == num_close:
                max_len = max(max_len, num_close + num_open)
            elif num_open > num_close:
                num_open = 0
                num_close = 0
        return max_len
