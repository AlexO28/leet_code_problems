# Design a data structure to find the frequency of a given value in a given subarray.
# The frequency of a value in a subarray is the number of occurrences of that value in the subarray.
# Implement the RangeFreqQuery class:
# RangeFreqQuery(int[] arr) Constructs an instance of the class with the given 0-indexed integer array arr.
# int query(int left, int right, int value) Returns the frequency of value in the subarray arr[left...right].
# A subarray is a contiguous sequence of elements within an array. arr[left...right] denotes the subarray that contains the elements of nums between indices left and right (inclusive).
import bisect
from typing import List
from functools import cache


class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.inverted_index = {}
        for j in range(len(arr)):
            if arr[j] in self.inverted_index:
                self.inverted_index[arr[j]].append(j)
            else:
                self.inverted_index[arr[j]] = [j]

    @cache
    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.inverted_index:
            return 0
        first_index = bisect.bisect_left(self.inverted_index[value], left)
        if first_index >= len(self.inverted_index[value]):
            return 0
        last_index = bisect.bisect_right(self.inverted_index[value], right) - 1
        if last_index < 0:
            return 0
        return len(self.inverted_index[value][first_index : (last_index + 1)])


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
