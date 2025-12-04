# Given an array of positive integers arr, find a pattern of length m that is repeated k or more times.
# A pattern is a subarray (consecutive sub-sequence) that consists of one or more values, repeated multiple times consecutively without overlapping. A pattern is defined by its length and the number of repetitions.
# Return true if there exists a pattern of length m that is repeated k or more times, otherwise return false.
from typing import List


class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        mk = m * k
        if len(arr) < mk:
            return False
        for start in range(len(arr) - mk + 1):
            if arr[start : start + mk] == arr[start : start + m] * k:
                return True
        return False
