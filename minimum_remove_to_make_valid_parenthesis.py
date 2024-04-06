# Given a string s of '(' , ')' and lowercase English characters.
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
# Formally, a parentheses string is valid if and only if:
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        num_open = 0
        num_close = 0
        indices_to_delete = []
        for j in range(len(s)):
            if s[j] == '(':
                num_open += 1
            elif s[j] == ')':
                num_close += 1
                if num_close > num_open:
                    num_close -= 1
                    indices_to_delete.append(j)
        if len(indices_to_delete) > 0:
            for ind in indices_to_delete[::-1]:
                del s[ind]
        if len(s) == 0:
            return ''.join(s)
        num_open = 0
        num_close = 0
        indices_to_delete = []
        for j in range(len(s)):
            if s[len(s)-j-1] == ")":
                num_close += 1
            elif s[len(s)-j-1] == "(":
                num_open += 1
                if num_open > num_close:
                    num_open -= 1
                    indices_to_delete.append(len(s)-j-1)
        if len(indices_to_delete) > 0:
            for ind in indices_to_delete:
                del s[ind]
        return ''.join(s)
