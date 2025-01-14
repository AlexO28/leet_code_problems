# You are given two 0-indexed integer permutations A and B of length n.
# A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.
# Return the prefix common array of A and B.
# A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.
from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        if len(A) == 1:
            return [1]
        res = []
        freq_dict = {}
        prev_res = 0
        for j in range(len(A)):
            if A[j] in freq_dict:
                freq_dict[A[j]] += 1
                prev_res += 1
            else:
                freq_dict[A[j]] = 1
            if B[j] in freq_dict:
                freq_dict[B[j]] += 1
                prev_res += 1
            else:
                freq_dict[B[j]] = 1
            res.append(prev_res)
        return res
