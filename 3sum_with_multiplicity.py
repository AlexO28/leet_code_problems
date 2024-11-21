# Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.
# As the answer can be very large, return it modulo 109 + 7.
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        freq_dict = {}
        for elem in arr:
            if elem in freq_dict:
                freq_dict[elem] += 1
            else:
                freq_dict[elem] = 1
        res = 0
        MOD = 10 ** 9 + 7
        for j in range(len(arr)):
            freq_dict[arr[j]] -= 1
            for i in range(j):
                val = target - arr[j] - arr[i]
                if val in freq_dict:
                    res = (res + freq_dict[val]) % MOD
        return res
