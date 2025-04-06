# Given a matrix and a target, return the number of non-empty submatrices that sum to target.
# A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.
# Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.
from typing import List


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        total_count = 0
        for start_row in range(len(matrix)):
            column_sums = [0] * (len(matrix[0]))
            for end_row in range(start_row, len(matrix)):
                for col in range(len(matrix[0])):
                    column_sums[col] += matrix[end_row][col]
                total_count += self.countSubarraysWithTargetSum(column_sums, target)
        return total_count
        
    def countSubarraysWithTargetSum(self, nums, target):
        prefix_sum_counts = {0: 1}
        count = 0
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            delta = prefix_sum - target
            if delta in prefix_sum_counts:
                count += prefix_sum_counts[delta]
            if prefix_sum in prefix_sum_counts:
                prefix_sum_counts[prefix_sum] += 1
            else:
                prefix_sum_counts[prefix_sum] = 1
        return count
