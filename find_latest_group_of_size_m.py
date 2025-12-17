# Given an array arr that represents a permutation of numbers from 1 to n.
# You have a binary string of size n that initially has all its bits set to zero. At each step i (assuming both the binary string and arr are 1-indexed) from 1 to n, the bit at position arr[i] is set to 1.
# You are also given an integer m. Find the latest step at which there exists a group of ones of length m. A group of ones is a contiguous substring of 1's such that it cannot be extended in either direction.
# Return the latest step at which there exists a group of ones of length exactly m. If no such group exists, return -1.
from typing import List


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if len(arr) == 1:
            return 1
        if m == len(arr):
            return len(arr)
        cnt = [0] * (len(arr) + 2)
        res = -1
        for i, v in enumerate(arr):
            v -= 1
            l = cnt[v - 1]
            r = cnt[v + 1]
            if (l == m) or (r == m):
                res = i
            cnt[v + r] = l + r + 1
            cnt[v - l] = cnt[v + r]
        return res
