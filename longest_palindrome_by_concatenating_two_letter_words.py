# You are given an array of strings words. Each element of words consists of two lowercase English letters.
# Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.
# Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.
# A palindrome is a string that reads the same forward and backward.
from typing import List
from collections import Counter


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq_dict = Counter(words)
        if len(freq_dict) == 1:
            key = list(freq_dict.keys())[0]
            if key[0] == key[1]:
                return 2 * freq_dict[key]
            else:
                return 0
        found = False
        res = 0
        for elem in freq_dict:
            if elem[0] == elem[1]:
                main_part, remainder = divmod(freq_dict[elem], 2)
                if not found:
                    found = (remainder == 1)
                res += 4 * main_part
            else:
                if elem[0] < elem[1]:
                    inverse_elem = elem[::-1]
                    if inverse_elem in freq_dict:
                        res += 4 * (min(freq_dict[elem], freq_dict[inverse_elem]))
        if found:
            return res + 2
        else:
            return res
