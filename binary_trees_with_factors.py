# Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.
# We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.
# Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        index_by_value = {arr[j]: j for j in range(len(arr))}
        dp = [1]*(len(arr))
        for i in range(len(arr)):
            for j in range(i):
                a = arr[i]
                b = arr[j]
                if a % b == 0:
                    c = a // b
                    if c in index_by_value:
                        dp[i] = (dp[i] + dp[j]*dp[index_by_value[c]]) % MOD
        return sum(dp) % MOD
