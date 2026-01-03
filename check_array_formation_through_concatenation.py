# You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].
# Return true if it is possible to form the array arr from pieces. Otherwise, return false.
from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        d = {p[0]: p for p in pieces}
        i = 0
        while i < len(arr):
            if arr[i] not in d:
                return False
            p = d[arr[i]]
            if arr[i : i + len(p)] != p:
                return False
            i += len(p)
        return True
