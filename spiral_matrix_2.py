# Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.


def initialize(n):
    mat = []
    for i in range(n):
        elem = []
        for j in range(n):
            elem.append(0)
        mat.append(elem)
    return mat


def spiralOrder(matrix):
    n = len(matrix)
    start_x = 0
    start_y = 0
    counter = 1
    while True:
        if n-start_y > start_y:
            for i in range(start_y, n - start_y):
                matrix[start_x][i] = counter
                counter += 1
        else:
            break
        if n-start_x > start_x+1:
            for i in range(start_x + 1, n - start_x):
                matrix[i][n - start_y - 1] = counter
                counter += 1
        else:
            break
        if n - start_x - 1 != start_x:
            for i in range(start_y + 1, n - start_y):
                matrix[n - start_x - 1][n - i - 1] = counter
                counter += 1
        if start_y != n - start_y - 1:
            for i in range(start_x + 1, n - start_x - 1):
                matrix[n - i - 1][start_y] = counter
                counter += 1
        if start_x + 1 == n - start_x - 1:
            break
        if start_y + 1 == n - start_y - 1:
            break
        start_y = start_y + 1
        start_x = start_x + 1
    return matrix


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = initialize(n)
        return spiralOrder(mat)
