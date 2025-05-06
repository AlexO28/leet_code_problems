# Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.
# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
# a, b are from arr
# a < b
# b - a equals to the minimum absolute difference of any two elements in arr
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_diff = arr[1] - arr[0]
        for j in range(1, len(arr)):
            min_diff = min(min_diff, arr[j] - arr[j - 1])
        res = []
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
                if arr[j] - arr[i] > min_diff:
                    break
                else:
                    res.append([arr[i], arr[j]])
        return res
