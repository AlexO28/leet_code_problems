# You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.
# Return the minimum size of the set so that at least half of the integers of the array are removed.
from typing import List
from collections import Counter


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq_dict = Counter(arr)
        values = list(freq_dict.values())
        values.sort(reverse=True)
        summa = 0
        size = 0
        for j in range(len(values)):
            summa += values[j]
            size += 1
            if summa >= len(arr) // 2:
                break
        return size
