# Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.
# Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        counter = 0
        for i in range(len(board)):
            found_ship = False 
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    if i > 0:
                        if board[i-1][j] != "X":
                            found_ship = True
                    else:
                        found_ship = True
                else:
                    if found_ship:
                        found_ship = False
                        counter += 1
            if found_ship:
                counter += 1
        return counter
        
