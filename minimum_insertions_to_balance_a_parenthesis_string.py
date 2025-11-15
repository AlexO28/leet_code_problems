# Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:
# Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
# Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
# In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.
# For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.
# You can insert the characters '(' and ')' at any position of the string to balance it if needed.
# Return the minimum number of insertions needed to make s balanced.
class Solution:
    def minInsertions(self, s: str) -> int:
        s = list(s)
        brackets = 0
        j = 0
        res = 0
        while j < len(s):
            if s[j] == "(":
                brackets += 1
                j += 1
            else:
                if j < len(s) - 1:
                    if s[j + 1] == "(":
                        res += 1
                        j += 1
                    else:
                        j += 2
                    if brackets == 0:
                        res += 1
                    else:
                        brackets -= 1
                else:
                    res += 1
                    if brackets == 0:
                        res += 1
                    else:
                        brackets -= 1
                    j += 1
        return res + 2 * brackets
