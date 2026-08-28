# You are given two strings s and t. In one step, you can append any character to either s or t.
# Return the minimum number of steps to make s and t anagrams of each other.
# An anagram of a string is a string that contains the same characters with a different (or the same) ordering.
from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freq_dict_1 = Counter(s)
        freq_dict_2 = Counter(t)
        min_steps = 0
        for key in freq_dict_1:
            if key in freq_dict_2:
                min_steps += abs(freq_dict_1[key] - freq_dict_2[key])
            else:
                min_steps += freq_dict_1[key]
        for key in freq_dict_2:
            if key not in freq_dict_1:
                min_steps += freq_dict_2[key] 
        return min_steps
