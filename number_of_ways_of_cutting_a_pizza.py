# Given a rectangular pizza represented as a rows x cols matrix containing the following characters: 'A' (an apple) and '.' (empty cell) and given the integer k. You have to cut the pizza into k pieces using k-1 cuts. 
# For each cut you choose the direction: vertical or horizontal, then you choose a cut position at the cell boundary and cut the pizza into two pieces. If you cut the pizza vertically, give the left part of the pizza to a person. If you cut the pizza horizontally, give the upper part of the pizza to a person. Give the last piece of pizza to the last person.
# Return the number of ways of cutting the pizza such that each piece contains at least one apple. Since the answer can be a huge number, return this modulo 10^9 + 7.
from functools import cache
from typing import List


class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        self.MOD = 10**9 + 7
        self.rows, self.cols = len(pizza), len(pizza[0])
        self.prefix_sum = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]
        for row in range(1, self.rows + 1):
            for col in range(1, self.cols + 1):
                self.prefix_sum[row][col] = (
                    self.prefix_sum[row - 1][col]
                    + self.prefix_sum[row][col - 1]
                    - self.prefix_sum[row - 1][col - 1]
                    + int(pizza[row - 1][col - 1] == "A")
                )
        return self.count_ways(0, 0, k - 1)

    @cache
    def count_ways(self, top_row: int, left_col: int, cuts_remaining: int) -> int:
        if cuts_remaining == 0:
            apples_in_piece = (
                self.prefix_sum[self.rows][self.cols]
                - self.prefix_sum[top_row][self.cols]
                - self.prefix_sum[self.rows][left_col]
                + self.prefix_sum[top_row][left_col]
            )
            return 1 if apples_in_piece > 0 else 0
        total_ways = 0
        for cut_row in range(top_row + 1, self.rows):
            apples_in_top = (
                self.prefix_sum[cut_row][self.cols]
                - self.prefix_sum[top_row][self.cols]
                - self.prefix_sum[cut_row][left_col]
                + self.prefix_sum[top_row][left_col]
            )
            if apples_in_top > 0:
                total_ways += self.count_ways(cut_row, left_col, cuts_remaining - 1)
        for cut_col in range(left_col + 1, self.cols):
            apples_in_left = (
                self.prefix_sum[self.rows][cut_col]
                - self.prefix_sum[top_row][cut_col]
                - self.prefix_sum[self.rows][left_col]
                + self.prefix_sum[top_row][left_col]
            )
            if apples_in_left > 0:
                total_ways += self.count_ways(top_row, cut_col, cuts_remaining - 1)
        return total_ways % self.MOD
