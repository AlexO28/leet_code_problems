# Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.
# Return the largest lucky integer in the array. If there is no lucky integer return -1.
from typing import List
from collections import Counter


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq_dict = Counter(arr)
        keys = list(freq_dict.keys())
        keys.sort(reverse=True)
        for key in keys:
            if freq_dict[key] == key:
                return key
        return -1
