# You are given two string arrays words1 and words2.
# A string b is a subset of string a if every letter in b occurs in a including multiplicity.
# For example, "wrr" is a subset of "warrior" but is not a subset of "world".
# A string a from words1 is universal if for every string b in words2, b is a subset of a.
# Return an array of all the universal strings in words1. You may return the answer in any order.
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        large_freq_dict = {}
        for word in words2:
            freq_dict = self.word_to_freq_dict(word)
            for letter in freq_dict:
                if letter not in large_freq_dict:
                    large_freq_dict[letter] = freq_dict[letter]
                else:
                    large_freq_dict[letter] = max(large_freq_dict[letter], freq_dict[letter])
        res = []
        for word in words1:
            is_universal = True
            freq_dict = self.word_to_freq_dict(word)
            for letter in large_freq_dict:
                if letter not in freq_dict:
                    is_universal = False
                    break
                else:
                    if freq_dict[letter] < large_freq_dict[letter]:
                        is_universal = False
                        break
            if is_universal:
                res.append(word)
        return res


    def word_to_freq_dict(self, word):
        freq_dict = {}
        for letter in list(word):
            if letter in freq_dict:
                freq_dict[letter] += 1
            else:
                freq_dict[letter] = 1
        return freq_dict
