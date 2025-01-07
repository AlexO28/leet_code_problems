# Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.
from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return []
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    if words[i] in words[j]:
                        res.append(words[i])
        return list(set(res))
