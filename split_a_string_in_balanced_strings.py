# Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
# Given a balanced string s, split it into some number of substrings such that:
# Each substring is balanced.
# Return the maximum number of balanced strings you can obtain.
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        balance = 0
        for elem in s:
            if elem == "L":
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                res += 1
        return res
