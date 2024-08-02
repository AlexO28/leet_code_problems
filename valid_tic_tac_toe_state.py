# Given a Tic-Tac-Toe board as a string array board, return true if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.
# The board is a 3 x 3 array that consists of characters ' ', 'X', and 'O'. The ' ' character represents an empty square.
# Here are the rules of Tic-Tac-Toe:
# Players take turns placing characters into empty squares ' '.
# The first player always places 'X' characters, while the second player always places 'O' characters.
# 'X' and 'O' characters are always placed into empty squares, never filled ones.
# The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        countX = sum(row.count('X') for row in board)
        countO = sum(row.count('O') for row in board)
        self.board = board
        if (countX < countO) or (countX - countO > 1):
            return False
        elif (self.isWin('X') and countX == countO) or (self.isWin('O') and countX != countO):
            return False
        else:
            return True

    def isWin(self, cell):
        return any(row.count(cell) == 3 for row in self.board) or \
            any(row.count(cell) == 3 for row in list(zip(*self.board))) or \
            all(self.board[i][i] == cell for i in range(3)) or \
            all(self.board[i][2 - i] == cell for i in range(3))
