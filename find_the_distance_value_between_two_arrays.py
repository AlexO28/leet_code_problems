# Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.
# The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.
import bisect
from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        res = 0
        for elem in arr1:
            index = bisect.bisect_left(arr2, elem)
            if (index >= 0) and (index < len(arr2)):
                if abs(elem - arr2[index]) <= d:
                    continue
            index += 1
            if (index >= 0) and (index < len(arr2)):
                if abs(elem - arr2[index]) <= d:
                    continue
            index -= 2
            if (index >= 0) and (index < len(arr2)):
                if abs(elem - arr2[index]) <= d:
                    continue
            res += 1
        return res
