# Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        res = []
        for j in range(len(arr)):
            res.append(arr[j])
            if arr[j] == 0:
                res.append(0)
        for j in range(len(arr)):
            arr[j] = res[j]
