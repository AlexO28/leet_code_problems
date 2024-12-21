# Given an integer array of even length arr, return true if it is possible to reorder arr such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2, or false otherwise.
from typing import List
from collections import Counter


class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        frequencies = Counter(arr)
        if frequencies[0] % 2 != 0:
            return False
        elements = sorted(frequencies, key=abs)
        for element in elements:
            double_element = 2 * element
            if frequencies[double_element] < frequencies[element]:
                return False
            frequencies[double_element] -= frequencies[element]
        return True
