# You are given a 0-indexed array arr consisting of n positive integers, and a positive integer k.
# The array arr is called K-increasing if arr[i-k] <= arr[i] holds for every index i, where k <= i <= n-1.
# However, the same arr is not K-increasing for k = 1 (because arr[0] > arr[1]) or k = 3 (because arr[0] > arr[3]).
# In one operation, you can choose an index i and change arr[i] into any positive integer.
# Return the minimum number of operations required to make the array K-increasing for the given k.
from typing import List
from bisect import bisect_right


class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        return sum(self.process(arr[i::k]) for i in range(k))

    def process(self, arr):
        t = []
        for x in arr:
            idx = bisect_right(t, x)
            if idx == len(t):
                t.append(x)
            else:
                t[idx] = x
        return len(arr) - len(t)
