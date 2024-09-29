# Given an integer array nums and an integer k, return the length of the shortest non-empty subarray of nums with a sum of at least k. If there is no such subarray, return -1.
# A subarray is a contiguous part of an array.
from collections import deque
from itertools import accumulate


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix_sums = list(accumulate(nums, initial=0))
        indices_deque = deque()
        min_length = -1
        for j in range(len(prefix_sums)):
            while indices_deque and prefix_sums[j] - prefix_sums[indices_deque[0]] >= k:
                if min_length < 0:
                    min_length = j - indices_deque.popleft()
                else:
                    min_length = min(min_length, j - indices_deque.popleft())
            while indices_deque and prefix_sums[indices_deque[-1]] >= prefix_sums[j]:
                indices_deque.pop()
            indices_deque.append(j)
        return min_length
