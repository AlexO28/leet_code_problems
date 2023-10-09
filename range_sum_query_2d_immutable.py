# Given a 2D matrix matrix, handle multiple queries of the following type:
# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# Implement the NumMatrix class:
# NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
# int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.dict = {}
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        summa = 0
        for row in range(row1, row2+1):
            if (row, col1, col2) in self.dict.keys():
                summa += self.dict[(row, col1, col2)]
            else:
                num = sum(self.matrix[row][col1:(col2+1)])
                self.dict[(row, col1, col2)] = num
                summa += num
        return summa
