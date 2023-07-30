class Solution:
    def markNeighbors(self, board, i, j, m, n):
        if i-1 > 0:
            if board[i-1][j] == 'O':
                board[i-1][j] = 'Z'
                self.markNeighbors(board, i-1, j, m, n)
        if i+1 < m:
            if board[i+1][j] == 'O':
                board[i+1][j] = 'Z'
                self.markNeighbors(board, i+1, j, m, n)
        if j-1 > 0:
            if board[i][j-1] == 'O':
                board[i][j-1] = 'Z'
                self.markNeighbors(board, i, j-1, m, n)
        if j+1 < n:
            if board[i][j+1] == 'O':
                board[i][j+1] = 'Z'
                self.markNeighbors(board, i, j+1, m, n)


    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        if (m > 1) and (n > 1):
            for i in range(m):
                if board[i][0] == 'O':
                    board[i][0] = 'Z'
                    self.markNeighbors(board, i, 0, m, n)
                if board[i][n-1] == 'O':
                    board[i][n-1] = 'Z'
                    self.markNeighbors(board, i, n-1, m, n)
            for i in range(n):
                if board[0][i] == 'O':
                    board[0][i] = 'Z'
                    self.markNeighbors(board, 0, i, m, n)
                if board[m-1][i] == 'O':
                    board[m-1][i] = 'Z'
                    self.markNeighbors(board, m-1, i, m, n)
            for i in range(m):
                for j in range(n):
                    if board[i][j] == 'O':
                        board[i][j] = 'X'
                    elif board[i][j] == 'Z':
                        board[i][j] = 'O'
