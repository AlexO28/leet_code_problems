# A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.
# Given a row x col grid of integers, how many 3 x 3 magic square subgrids are there?
# Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if (len(grid) < 3) or (len(grid[0]) < 3):
            return 0
        number_of_magic_squares = 0
        for i in range(len(grid)-2):
            for j in range(len(grid[0])-2):
                if self.isMagicSquare(grid, i, j):
                    number_of_magic_squares += 1
        return number_of_magic_squares

    def isMagicSquare(self, grid, i, j):
        arr = []
        for x in range(i, i+3):
            for y in range(j, j+3):
                if (grid[x][y] > 9) or (grid[x][y] == 0):
                    return False
                arr.append(grid[x][y])
        if len(list(set(arr))) < 9:
            return False
        summa = grid[i][j] + grid[i][j+1] + grid[i][j+2]
        if grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2] != summa:
            return False
        if grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2] != summa:
            return False
        if grid[i][j] + grid[i+1][j] + grid[i+2][j] != summa:
            return False
        if grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1] != summa:
            return False
        if grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2] != summa:
            return False
        if grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] != summa:
            return False
        if grid[i+2][j] + grid[i+1][j+1] + grid[i][j+2] != summa:
            return False
        return True
