# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.


import numpy as np


def check_array(arr):
    dict = {}
    for elem in arr:
        if elem not in ['.', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return False
        if elem != '.':
            if elem in dict.keys():
                return False
            else:
                dict[elem] = 1
    return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        tab = np.array(board)
        for j in range(9):
            if not check_array(tab[:,j]):
                return False
            if not check_array(tab[j,:]):
                return False
        for i in range(3):
            for j in range(3):
                temp_list = tab[(3*i): (3*(i+1)), (3*j): (3*(j+1))].tolist()
                temp_list = temp_list[0] + temp_list[1] + temp_list[2]
                if not check_array(temp_list):
                    return False
        return True
