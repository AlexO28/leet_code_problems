# You are given a 0-indexed array of n integers differences, which describes the differences between each pair of consecutive integers of a hidden sequence of length (n + 1). More formally, call the hidden sequence hidden, then we have that differences[i] = hidden[i + 1] - hidden[i].
# You are further given two integers lower and upper that describe the inclusive range of values [lower, upper] that the hidden sequence can contain.
# Return the number of possible hidden sequences there are. If there are no possible sequences, return 0.
from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_val = 0
        max_val = 0
        cur_val = 0
        for j in range(len(differences)):
            cur_val += differences[j]
            min_val = min(min_val, cur_val)
            max_val = max(max_val, cur_val)
        return max(upper - lower + 1 - max_val + min_val, 0)
