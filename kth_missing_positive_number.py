# Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
# Return the kth positive integer that is missing from this array.
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr = set(arr)
        count = 0
        num = 0
        for i in range(1, 2001):
            if i not in arr:
                count += 1
                num = i
                if count == k:
                    return num
        return num
