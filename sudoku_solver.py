# Write a program to solve a Sudoku puzzle by filling the empty cells.
# A sudoku solution must satisfy all of the following rules:
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.row_used = [[False] * 9 for _ in range(9)]
        self.col_used = [[False] * 9 for _ in range(9)]
        self.block_used = [[[False] * 9 for _ in range(3)] for _ in range(3)]
        self.empty_cells = []
        self.board = board
        self.solved = False
        for row_idx in range(9):
            for col_idx in range(9):
                if self.board[row_idx][col_idx] == ".":
                    self.empty_cells.append((row_idx, col_idx))
                else:
                    digit = int(board[row_idx][col_idx]) - 1
                    self.row_used[row_idx][digit] = True
                    self.col_used[col_idx][digit] = True
                    self.block_used[row_idx // 3][col_idx // 3][digit] = True
        self.backtrack(0)

    def backtrack(self, index):
        if index == len(self.empty_cells):
            self.solved = True
        else:
            row_idx, col_idx = self.empty_cells[index]
            for digit in range(9):
                if (
                    not self.row_used[row_idx][digit]
                    and not self.col_used[col_idx][digit]
                    and not self.block_used[row_idx // 3][col_idx // 3][digit]
                ):
                    self.row_used[row_idx][digit] = True
                    self.col_used[col_idx][digit] = True
                    self.block_used[row_idx // 3][col_idx // 3][digit] = True
                    self.board[row_idx][col_idx] = str(digit + 1)
                    self.backtrack(index + 1)
                    if self.solved:
                        break
                    self.row_used[row_idx][digit] = False
                    self.col_used[col_idx][digit] = False
                    self.block_used[row_idx // 3][col_idx // 3][digit] = False
