# Given an array of integers arr, return true if and only if it is a valid mountain array.
# Recall that arr is a mountain array if and only if:
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        if arr[1] <= arr[0]:
            return False
        increasing = True
        for j in range(1, len(arr)):
            if increasing:
                if arr[j] == arr[j-1]:
                    return False
                if arr[j] < arr[j-1]:
                    increasing = False
            else:
                if arr[j] >= arr[j-1]:
                    return False
        if increasing:
            return False
        return True
