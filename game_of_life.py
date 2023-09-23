# The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        neighbors = []
        for i in range(m):
            temp = []
            for j in range(n):
                number_of_neighbors = self.calculateNumberOfNeighbors(i, j, m, n, board)
                temp.append(number_of_neighbors)
            neighbors.append(temp)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 1:
                    if (neighbors[i][j] < 2) or (neighbors[i][j] > 3):
                        board[i][j] = 0 
                else:
                    if neighbors[i][j] == 3:
                        board[i][j] = 1


    def calculateNumberOfNeighbors(self, i, j, m, n, board):
        number_of_neighbors = 0
        if (i > 0) and (j > 0):
            number_of_neighbors += board[i-1][j-1]
        if i > 0:
            number_of_neighbors += board[i-1][j]
        if (i > 0) and (j < n-1):
            number_of_neighbors += board[i-1][j+1]
        if j > 0:
            number_of_neighbors += board[i][j-1]
        if j < n-1:
            number_of_neighbors += board[i][j+1]
        if (i < m-1) and (j > 0):
            number_of_neighbors += board[i+1][j-1]
        if i < m-1:
            number_of_neighbors += board[i+1][j]
        if (i < m-1) and (j < n-1):
            number_of_neighbors += board[i+1][j+1]
        return number_of_neighbors
 
Console
