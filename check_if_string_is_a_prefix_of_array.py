# Given a string s and an array of strings words, determine whether s is a prefix string of words.
# A string s is a prefix string of words if s can be made by concatenating the first k strings in words for some positive k no larger than words.length.
# Return true if s is a prefix string of words, or false otherwise.
from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        res = ""
        for word in words:
            res += word
            if len(res) > len(s):
                return False
            if res == s:
                return True
            if len(res) == len(s):
                return False
        return False
