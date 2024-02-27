# Let's play the minesweeper game (Wikipedia, online game)!
# You are given an m x n char matrix board representing the game board where:
# 'M' represents an unrevealed mine,
# 'E' represents an unrevealed empty square,
# 'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
# digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
# 'X' represents a revealed mine.
# You are also given an integer array click where click = [clickr, clickc] represents the next click position among all the unrevealed squares ('M' or 'E').
# Return the board after revealing this position according to the following rules:
# If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
# If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
# If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
# Return the board when no more squares will be revealed.
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.checkCell(board, click)
        return board

    def checkCell(self, board, click):
        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
        elif board[click[0]][click[1]] == "E":
            number_of_mines = 0
            if (click[0] > 0) & (click[1] > 0):
                if board[click[0]-1][click[1]-1] == "M":
                    number_of_mines += 1
            if click[0] > 0:
                if board[click[0]-1][click[1]] == "M":
                    number_of_mines += 1
            if (click[0] > 0) & (click[1] < len(board[0])-1):
                if board[click[0]-1][click[1]+1] == "M":
                    number_of_mines += 1
            if (click[1] < len(board[0])-1):
                if board[click[0]][click[1]+1] == "M":
                    number_of_mines += 1
            if (click[1] < len(board[0])-1) & (click[0] < len(board)-1):
                if board[click[0]+1][click[1]+1] == "M":
                    number_of_mines += 1
            if (click[0] < len(board)-1):
                if board[click[0]+1][click[1]] == "M":
                    number_of_mines += 1
            if (click[0] < len(board)-1) & (click[1] > 0):
                if board[click[0]+1][click[1]-1] == "M":
                    number_of_mines += 1
            if click[1] > 0:
                if board[click[0]][click[1]-1] == "M":
                    number_of_mines += 1
            if number_of_mines > 0:
                board[click[0]][click[1]] = str(number_of_mines)
            else:
                board[click[0]][click[1]] = "B"
                if (click[0] > 0) & (click[1] > 0):
                    self.checkCell(board, [click[0]-1, click[1]-1])
                if click[0] > 0:
                    self.checkCell(board, [click[0]-1, click[1]])
                if (click[0] > 0) & (click[1] < len(board[0])-1):
                    self.checkCell(board, [click[0]-1, click[1]+1])
                if (click[1] < len(board[0])-1):
                    self.checkCell(board, [click[0], click[1]+1])
                if (click[1] < len(board[0])-1) & (click[0] < len(board)-1):
                    self.checkCell(board, [click[0]+1, click[1]+1])
                if (click[0] < len(board)-1):
                    self.checkCell(board, [click[0]+1, click[1]])
                if (click[0] < len(board)-1) & (click[1] > 0):
                    self.checkCell(board, [click[0]+1, click[1]-1])
                if click[1] > 0:
                    self.checkCell(board, [click[0], click[1]-1])
