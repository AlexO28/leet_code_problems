# Given a 2D integer array matrix, return the transpose of matrix.
# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new_matrix = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(n):
            temp = []
            for j in range(m):
                temp.append(matrix[j][i])
            new_matrix.append(temp)
        return new_matrix
