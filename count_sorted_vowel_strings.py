# Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.
# A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.
from functools import cache


class Solution:
    def countVowelStrings(self, n: int) -> int:
        return self.count(n, "a")

    @cache
    def count(self, n, last_character):
        if n == 1:
            if last_character == "a":
                return 5
            elif last_character == "e":
                return 4
            elif last_character == "i":
                return 3
            elif last_character == "o":
                return 2
            else:
                return 1
        else:
            res = 0
            for symbol in ["a", "e", "i", "o", "u"]:
                if symbol >= last_character:
                    res += self.count(n - 1, symbol)
            return res
