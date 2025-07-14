# Given a string s. Return all the words vertically in the same order in which they appear in s.
# Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
# Each word would be put on only one column and that in one column there will be only one word.
from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(" ")
        new_words = []
        max_len = 0
        for word in words:
            if len(word) > 0:
                new_words.append(word)
                max_len = max(max_len, len(word))
        res = [[] * max_len for j in range(max_len)]
        for i in range(len(words)):
            for j in range(len(words[i])):
                res[j].append(words[i][j])
            if len(words[i]) < max_len:
                for j in range(len(words[i]), max_len):
                    res[j].append(" ")
        return ["".join(elem).rstrip() for elem in res]
