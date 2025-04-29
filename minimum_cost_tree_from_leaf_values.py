# Given an array arr of positive integers, consider all binary trees such that:
# Each node has either 0 or 2 children;
# The values of arr correspond to the values of each leaf in an in-order traversal of the tree.
# The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree, respectively.
# Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node. It is guaranteed this sum fits into a 32-bit integer.
# A node is a leaf if and only if it has zero children.
from math import inf
from typing import List


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        dp = [[0] * len(arr) for i in range(len(arr))]
        max_matrix = [[0]  * len(arr) for i in range(len(arr))]
        for start in range(len(arr) - 1, -1, -1):
            max_matrix[start][start] = arr[start]
            for end in range(start + 1, len(arr)):
                max_matrix[start][end] = max(max_matrix[start][end-1], arr[end])
                dp[start][end] = inf
                for k in range(start, end):
                    dp[start][end] = min(dp[start][end], dp[start][k] + dp[k + 1][end] + max_matrix[start][k] * max_matrix[k + 1][end])
        return dp[0][-1]
