# You may recall that an array arr is a mountain array if and only if:
# arr.length >= 3
# There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        res_length = 0
        left = 0
        while left < len(arr) - 2:
            right = left + 1
            if arr[left] < arr[right]:
                while (right < len(arr)-1) and (arr[right] < arr[right+1]):
                    right += 1
                if (right < len(arr) - 1) and (arr[right] > arr[right+1]):
                    while (right < len(arr)-1) and (arr[right] > arr[right+1]):
                        right += 1
                    res_length = max(res_length, right - left + 1)
                else:
                    right += 1
            left = right
        return res_length
