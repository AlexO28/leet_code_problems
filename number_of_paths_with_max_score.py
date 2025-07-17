# You are given a square board of characters. You can move on the board starting at the bottom right square marked with the character 'S'.
# You need to reach the top left square marked with the character 'E'. The rest of the squares are labeled either with a numeric character 1, 2, ..., 9 or with an obstacle 'X'. In one move you can go up, left or up-left (diagonally) only if there is no obstacle there.
# Return a list of two integers: the first integer is the maximum sum of numeric characters you can collect, and the second is the number of such paths that you can take to get that maximum sum, taken modulo 10^9 + 7.
# In case there is no path, return [0, 0].
from typing import List


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        self.board = board
        self.dp = [[-1] * (len(self.board)) for i in range(len(self.board))]
        self.count = [[0] * (len(self.board)) for i in range(len(self.board))]
        self.dp[-1][-1] = 0
        self.count[-1][-1] = 1
        for i in range(len(self.board) - 1, -1, -1):
            for j in range(len(self.board) - 1, -1, -1):
                self.update(i, j, i + 1, j)
                self.update(i, j, i, j + 1)
                self.update(i, j, i + 1, j + 1)
                if self.dp[i][j] != -1:
                    try:
                        self.dp[i][j] += int(board[i][j])
                    except:
                        continue
        if self.dp[0][0] == -1:
            return [0, 0]
        else:
            return [self.dp[0][0], self.count[0][0] % (10**9 + 7)]

    def update(self, i, j, next_i, next_j):
        if (
            (next_i >= len(self.board))
            or (next_j >= len(self.board))
            or (self.dp[next_i][next_j] == -1)
            or (self.board[i][j] in "XS")
        ):
            return
        if self.dp[next_i][next_j] > self.dp[i][j]:
            self.dp[i][j] = self.dp[next_i][next_j]
            self.count[i][j] = self.count[next_i][next_j]
        elif self.dp[next_i][next_j] == self.dp[i][j]:
            self.count[i][j] += self.count[next_i][next_j]
