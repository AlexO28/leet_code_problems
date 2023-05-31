# Given an m x n matrix, return all elements of the matrix in spiral order.


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m = len(matrix)
        n = len(matrix[0])
        start_x = 0
        start_y = 0
        while True:
            if n-start_y > start_y:
                for i in range(start_y, n - start_y):
                    res.append(matrix[start_x][i])
            else:
                break
            if m-start_x > start_x+1:
                for i in range(start_x + 1, m - start_x):
                    res.append(matrix[i][n - start_y - 1])
            else:
                break
            if m - start_x - 1 != start_x:
                for i in range(start_y + 1, n - start_y):
                    res.append(matrix[m - start_x - 1][n - i - 1])
            if start_y != n - start_y - 1:
                for i in range(start_x + 1, m - start_x - 1):
                    res.append(matrix[m - i - 1][start_y])
            if start_x + 1 == m - start_x - 1:
                break
            if start_y + 1 == n - start_y - 1:
                break
            start_y = start_y + 1
            start_x = start_x + 1
        return res
