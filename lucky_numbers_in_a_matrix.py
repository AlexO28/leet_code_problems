# Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_in_rows = []
        max_in_cols = []
        for i in range(len(matrix)):
            min_in_rows.append(min(matrix[i]))
        for j in range(len(matrix[0])):
            max_in_cols.append(max([matrix[i][j] for i in range(len(matrix))]))
        return [elem for elem in min_in_rows if elem in max_in_cols]
