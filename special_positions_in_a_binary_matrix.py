# Given an m x n binary matrix mat, return the number of special positions in mat.
# A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows_with_ones = {}
        cols_with_ones = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    if i in rows_with_ones:
                        rows_with_ones[i] += 1
                    else:
                        rows_with_ones[i] = 1
                    if j in cols_with_ones:
                        cols_with_ones[j] += 1
                    else:
                        cols_with_ones[j] = 1
        keys = list(rows_with_ones.keys()).copy()
        for key in keys:
            if rows_with_ones[key] > 1:
                del rows_with_ones[key]
        keys = list(cols_with_ones.keys()).copy()
        for key in keys:
            if cols_with_ones[key] > 1:
                del cols_with_ones[key]
        if (len(rows_with_ones.keys()) == 0) or (len(cols_with_ones.keys()) == 0):
            return 0
        number_of_ones = 0
        for row in rows_with_ones.keys():
            for col in cols_with_ones.keys():
                if mat[row][col] == 1:
                    number_of_ones += 1
                    break
        return number_of_ones
