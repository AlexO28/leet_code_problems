# Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
from functools import cmp_to_key


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        def compare(a, b):
            if a == b:
                return 0
            diff_1 = abs(a - x)
            diff_2 = abs(b - x)
            if (diff_1 < diff_2) or ((diff_1 == diff_2) and (a < b)):
                return -1
            else:
                return 1

        return sorted(sorted(arr, key=cmp_to_key(compare))[:k])
