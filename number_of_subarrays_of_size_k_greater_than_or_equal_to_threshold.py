# Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k and average greater than or equal to threshold.
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cur_mean = 0
        for j in range(k):
            cur_mean += arr[j] / k
        if cur_mean >= threshold:
            res = 1
        else:
            res = 0
        if k == len(arr):
            return res
        else:
            for j in range(k, len(arr)):
                cur_mean += arr[j] / k - arr[j - k] / k
                if cur_mean >= threshold:
                    res += 1
            return res
