# There is an 8 x 8 chessboard containing n pieces (rooks, queens, or bishops). You are given a string array pieces of length n, where pieces[i] describes the type (rook, queen, or bishop) of the ith piece. In addition, you are given a 2D integer array positions also of length n, where positions[i] = [ri, ci] indicates that the ith piece is currently at the 1-based coordinate (ri, ci) on the chessboard.
# When making a move for a piece, you choose a destination square that the piece will travel toward and stop on.
# A rook can only travel horizontally or vertically from (r, c) to the direction of (r+1, c), (r-1, c), (r, c+1), or (r, c-1).
# A queen can only travel horizontally, vertically, or diagonally from (r, c) to the direction of (r+1, c), (r-1, c), (r, c+1), (r, c-1), (r+1, c+1), (r+1, c-1), (r-1, c+1), (r-1, c-1).
# A bishop can only travel diagonally from (r, c) to the direction of (r+1, c+1), (r+1, c-1), (r-1, c+1), (r-1, c-1).
# You must make a move for every piece on the board simultaneously. A move combination consists of all the moves performed on all the given pieces. Every second, each piece will instantaneously travel one square towards their destination if they are not already at it. All pieces start traveling at the 0th second. A move combination is invalid if, at a given time, two or more pieces occupy the same square.
# Return the number of valid move combinations​​​​​.
# Notes:
# No two pieces will start in the same square.
# You may choose the square a piece is already on as its destination.
# If two pieces are directly adjacent to each other, it is valid for them to move past each other and swap positions in one second.
from typing import List


class Solution:
    def countCombinations(self, pieces: List[str], positions: List[List[int]]) -> int:
        self.rook_dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.bishop_dirs = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        self.queue_dirs = self.rook_dirs + self.bishop_dirs
        self.dist = [[[-1] * 9 for _ in range(9)] for _ in range(len(pieces))]
        self.end = [(0, 0, 0) for _ in range(len(pieces))]
        self.pieces = pieces
        self.positions = positions
        self.ans = 0
        self.search(0)
        return self.ans

    def search(self, i):
        if i >= len(self.pieces):
            self.ans += 1
        else:
            x, y = self.positions[i]
            self.dist[i][:] = [[-1] * 9 for _ in range(9)]
            self.dist[i][x][y] = 0
            self.end[i] = (x, y, 0)
            if self.check_stop(i, x, y, 0):
                self.search(i + 1)
            dirs = self.get_dirs(self.pieces[i])
            for dx, dy in dirs:
                self.dist[i][:] = [[-1] * 9 for _ in range(9)]
                self.dist[i][x][y] = 0
                nx = x + dx
                ny = y + dy
                nt = 1
                while 1 <= nx < 9 and 1 <= ny < 9 and self.check_pass(i, nx, ny, nt):
                    self.dist[i][nx][ny] = nt
                    self.end[i] = (nx, ny, nt)
                    if self.check_stop(i, nx, ny, nt):
                        self.search(i + 1)
                    nx += dx
                    ny += dy
                    nt += 1

    def check_stop(self, i, x, y, t):
        return all(self.dist[j][x][y] < t for j in range(i))

    def check_pass(self, i, x, y, t):
        for j in range(i):
            if self.dist[j][x][y] == t:
                return False
            if self.end[j][0] == x and self.end[j][1] == y and self.end[j][2] <= t:
                return False
        return True

    def get_dirs(self, piece):
        match piece[0]:
            case "r":
                return self.rook_dirs
            case "b":
                return self.bishop_dirs
            case _:
                return self.queue_dirs
