# Given an m x n matrix matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is no larger than k.
# It is guaranteed that there will be a rectangle with a sum no larger than k.
from sortedcontainers import SortedSet
from math import inf

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        max_sum = -inf
        for starting_row in range(num_rows):
            row_sums = [0] * num_cols
            for ending_row in range(starting_row, num_rows):
                for col in range(num_cols):
                    row_sums[col] += matrix[ending_row][col]
                current_sum = 0
                sorted_prefix_sums = SortedSet([0])
                for sum_value in row_sums:
                    current_sum += sum_value
                    index = sorted_prefix_sums.bisect_left(current_sum - k)
                    if index != len(sorted_prefix_sums):
                        if current_sum - sorted_prefix_sums[index] <= k:
                            max_sum = max(max_sum, current_sum - sorted_prefix_sums[index])
                            if max_sum == k:
                                return k
                    sorted_prefix_sums.add(current_sum)
        return max_sum
