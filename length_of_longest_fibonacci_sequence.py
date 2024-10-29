# A sequence x1, x2, ..., xn is Fibonacci-like if:
# n >= 3
# xi + xi+1 == xi+2 for all i + 2 <= n
# Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.
# A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        arr_dict = {arr[j]: j for j in range(len(arr))}
        dp = [[2 for i in range(len(arr))] for j in range(len(arr))]
        res = 0
        for i in range(len(arr)):
            for j in range(i):
                difference = arr[i] - arr[j]
                if difference in arr_dict:
                    prev_index = arr_dict[difference]
                    if prev_index < j:
                        dp[j][i] = max(dp[j][i], dp[prev_index][j] + 1)
                        res = max(res, dp[j][i])
        if res < 3:
            return 0
        else:
            return res