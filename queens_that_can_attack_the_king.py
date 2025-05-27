# On a 0-indexed 8 x 8 chessboard, there can be multiple black queens and one white king.
# You are given a 2D integer array queens where queens[i] = [xQueeni, yQueeni] represents the position of the ith black queen on the chessboard. You are also given an integer array king of length 2 where king = [xKing, yKing] represents the position of the white king.
# Return the coordinates of the black queens that can directly attack the king. You may return the answer in any order.
from typing import List


class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        res = []
        chessboard = [[0]*8 for i in range(8)]
        for queen in queens:
            chessboard[queen[0]][queen[1]] = 1
        if king[0] > 0:
            for i in range(king[0]-1, -1, -1):
                if chessboard[i][king[1]] == 1:
                    res.append([i, king[1]])
                    break
        if king[0] < 7:
            for i in range(king[0]+1, 8):
                if chessboard[i][king[1]] == 1:
                    res.append([i, king[1]])
                    break
        if king[1] > 0:
            for i in range(king[1]-1, -1, -1):
                if chessboard[king[0]][i] == 1:
                    res.append([king[0], i])
                    break
        if king[1] < 7:
            for i in range(king[1]+1, 8):
                if chessboard[king[0]][i] == 1:
                    res.append([king[0], i])
                    break
        for i in range(1, 8):
            posx = king[0] - i
            posy = king[1] - i
            if (posx >= 0) and (posy >= 0):
                if chessboard[posx][posy] == 1:
                    res.append([posx, posy])
                    break
        for i in range(1, 8):
            posx = king[0] + i
            posy = king[1] + i
            if (posx <= 7) and (posy <= 7):
                if chessboard[posx][posy] == 1:
                    res.append([posx, posy])
                    break
        for i in range(1, 8):
            posx = king[0] - i
            posy = king[1] + i
            if (posx >= 0) and (posy <= 7):
                if chessboard[posx][posy] == 1:
                    res.append([posx, posy])
                    break
        for i in range(1, 8):
            posx = king[0] + i
            posy = king[1] - i
            if (posx <= 7) and (posy >= 0):
                if chessboard[posx][posy] == 1:
                    res.append([posx, posy])
                    break
        return res
