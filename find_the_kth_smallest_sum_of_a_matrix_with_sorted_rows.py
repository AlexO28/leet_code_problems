# You are given an m x n matrix mat that has its rows sorted in non-decreasing order and an integer k.
# You are allowed to choose exactly one element from each row to form an array.
# Return the kth smallest array sum among all possible arrays.
from typing import List


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        previous_sums = [0]
        for current_row in mat:
            all_new_sums = []
            for prev_sum in previous_sums:
                for element in current_row[:k]:
                    all_new_sums.append(prev_sum + element)
            previous_sums = sorted(all_new_sums)[:k]
        return previous_sums[-1]
