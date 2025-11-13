# You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
# Return the shuffled string.
from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        s = list(s)
        new_s = [""] * len(s)
        for i in range(len(s)):
            new_s[indices[i]] = s[i]
        return "".join(new_s)
