# Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        MOD = 10 ** 9 + 7
        left = [-1]*(len(arr))
        right = [len(arr)]*(len(arr))
        indices = []
        for j in range(len(arr)):
            while (len(indices)>0) and (arr[indices[-1]] >= arr[j]):
                indices.pop()
            if len(indices) > 0:
                left[j] = indices[-1]
            indices.append(j)
        indices = []
        for j in range(len(arr)-1, -1, -1):
            while (len(indices)>0) and (arr[indices[-1]] > arr[j]):
                indices.pop()
            if len(indices) > 0:
                right[j] = indices[-1]
            indices.append(j)
        return sum([(j - left[j])*(right[j] - j)*arr[j] for j in range(len(arr))]) % MOD
