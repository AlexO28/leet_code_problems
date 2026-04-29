# The XOR sum of a list is the bitwise XOR of all its elements. If the list only contains one element, then its XOR sum will be equal to this element.
# For example, the XOR sum of [1,2,3,4] is equal to 1 XOR 2 XOR 3 XOR 4 = 4, and the XOR sum of [3] is equal to 3.
# You are given two 0-indexed arrays arr1 and arr2 that consist only of non-negative integers.
# Consider the list containing the result of arr1[i] AND arr2[j] (bitwise AND) for every (i, j) pair where 0 <= i < arr1.length and 0 <= j < arr2.length.
# Return the XOR sum of the aforementioned list.
from typing import List


class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        return self.calculateXorSum(arr1) & self.calculateXorSum(arr2)

    def calculateXorSum(self, arr):
        if len(arr) == 1:
            return arr[0]
        else:
            xorSum = arr[0]
            for j in range(1, len(arr)):
                xorSum ^= arr[j]
            return xorSum
