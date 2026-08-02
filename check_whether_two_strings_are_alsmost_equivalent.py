# Two strings word1 and word2 are considered almost equivalent if the differences between the frequencies of each letter from 'a' to 'z' between word1 and word2 is at most 3.
# Given two strings word1 and word2, each of length n, return true if word1 and word2 are almost equivalent, or false otherwise.
# The frequency of a letter x is the number of times it occurs in the string.
from collections import Counter


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        freq_dict_1 = Counter(word1)
        freq_dict_2 = Counter(word2)
        for key in "abcdefghijklmnopqrstuvwxyz":
            if abs(freq_dict_1.get(key, 0) - freq_dict_2.get(key, 0)) > 3:
                return False
        return True
