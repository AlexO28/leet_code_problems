# Write a program to solve a Sudoku puzzle by filling the empty cells.
# A sudoku solution must satisfy all of the following rules:
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.


def isValid(board, row, col, c):
    for i in range(9):
        if board[i][col] == c or board[row][i] == c:
          return False
    for i in range(3):
        for j in range(3):
            if board[3*(row // 3) + i][3*(col // 3) + j] == c:
                return False
    return True


def solve(board, i0, j0):
    if (i0 == 9) and (j0 == 0):
        return True
    if j0 == 8:
        i = i0 + 1
        j = 0
    else:
        i = i0
        j = j0 + 1
    if board[i0][j0] != '.':
        return solve(board, i, j)
    for c in range(1, 10):
        if isValid(board, i0, j0, str(c)):
            board[i0][j0] = str(c)
            if solve(board, i, j):
               return True
        board[i0][j0] = '.'
    return False


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        solve(board, 0, 0) 
