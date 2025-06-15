# Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:
# Players take turns placing characters into empty squares ' '.
# The first player A always places 'X' characters, while the second player B always places 'O' characters.
# 'X' and 'O' characters are always placed into empty squares, never on filled ones.
# The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
# Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. return the winner of the game if it exists (A or B). In case the game ends in a draw return "Draw". If there are still movements to play return "Pending".
# You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.
from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[-1] * 3 for i in range(3)]
        for i in range(len(moves)):
            if i % 2 == 0:
                board[moves[i][0]][moves[i][1]] = 1
            else:
                board[moves[i][0]][moves[i][1]] = 0
        if board[0][0] == board[0][1] == board[0][2]:
            if board[0][0] == 1:
                return "A"
            elif board[0][0] == 0:
                return "B"
        if board[1][0] == board[1][1] == board[1][2]:
            if board[1][0] == 1:
                return "A"
            elif board[1][0] == 0:
                return "B"
        if board[2][0] == board[2][1] == board[2][2]:
            if board[2][0] == 1:
                return "A"
            elif board[2][0] == 0:
                return "B"
        if board[0][0] == board[1][0] == board[2][0]:
            if board[0][0] == 1:
                return "A"
            elif board[0][0] == 0:
                return "B"
        if board[0][1] == board[1][1] == board[2][1]:
            if board[0][1] == 1:
                return "A"
            elif board[0][1] == 0:
                return "B"
        if board[0][2] == board[1][2] == board[2][2]:
            if board[0][2] == 1:
                return "A"
            elif board[0][2] == 0:
                return "B"
        if board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] == 1:
                return "A"
            elif board[0][0] == 0:
                return "B"
        if board[0][2] == board[1][1] == board[2][0]:
            if board[1][1] == 1:
                return "A"
            elif board[1][1] == 0:
                return "B"
        if len(moves) < 9:
            return "Pending"
        else:
            return "Draw"
