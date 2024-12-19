# You are given an 8 x 8 matrix representing a chessboard. There is exactly one white rook represented by 'R', some number of white bishops 'B', and some number of black pawns 'p'. Empty squares are represented by '.'.
# A rook can move any number of squares horizontally or vertically (up, down, left, right) until it reaches another piece or the edge of the board. A rook is attacking a pawn if it can move to the pawn's square in one move.
# Note: A rook cannot move through other pieces, such as bishops or pawns. This means a rook cannot attack a pawn if there is another piece blocking the path.
# Return the number of pawns the white rook is attacking.
from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        number_of_pawns = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    rook_x = i
                    rook_y = j
                    break
        if rook_x > 0:
            for i in range(rook_x-1, -1, -1):
                if board[i][rook_y] == "B":
                    break
                if board[i][rook_y] == "p":
                    number_of_pawns += 1
                    break
        if rook_x < 7:
            for i in range(rook_x+1, 8):
                if board[i][rook_y] == "B":
                    break
                if board[i][rook_y] == "p":
                    number_of_pawns += 1
                    break
        if rook_y > 0:
            for j in range(rook_y-1, -1, -1):
                if board[rook_x][j] == "B":
                    break
                if board[rook_x][j] == "p":
                    number_of_pawns += 1
                    break
        if rook_y < 7:
            for j in range(rook_y+1, 8):
                if board[rook_x][j] == "B":
                    break
                if board[rook_x][j] == "p":
                    number_of_pawns += 1
                    break
        return number_of_pawns
