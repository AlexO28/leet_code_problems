# Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.
# Formally, we can partition the array if we can find indexes i + 1 < j with (arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])
from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        target, remainder = divmod(sum(arr), 3)
        if remainder > 0:
            return False
        summa = 0
        found = -1
        for i in range(len(arr)):
            summa += arr[i]
            if summa == target:
                found = i
                break
        if (found < 0):
            return False
        summa = 0
        for j in range(found+1, len(arr)):
            summa += arr[j]
            if summa == target:
                if j < len(arr)-1:
                    return True
                else:
                    return False
        return False
