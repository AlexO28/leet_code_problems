# You are given an array of strings words and a string pref.
# Return the number of strings in words that contain pref as a prefix.
from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        for word in words:
            if len(word) >= len(pref):
                found = False
                for i in range(len(pref)):
                    if word[i] != pref[i]:
                        found = True
                        break
                if not found:
                    res += 1
        return res
