# Given an array of integers arr, sort the array by performing a series of pancake flips.
# In one pancake flip we do the following steps:
# Choose an integer k where 1 <= k <= arr.length.
# Reverse the sub-array arr[0...k-1] (0-indexed).
# Return an array of the k-values corresponding to a sequence of pancake flips that sort arr. Any valid answer that sorts the array within 10 * arr.length flips will be judged as correct.
from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return []
        flips = []
        for j in range(len(arr)-1, 0, -1):
            max_index = arr.index(j+1)
            if max_index != j:
                if max_index > 0:
                    flips.append(max_index + 1)
                    self.flip(arr, max_index)
                flips.append(j + 1)
                self.flip(arr, j)
        return flips


    def flip(self, arr, k):
        start = 0
        while start < k:
            arr[start], arr[k] = arr[k], arr[start]
            start += 1
            k -= 1
