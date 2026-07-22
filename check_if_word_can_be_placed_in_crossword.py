# You are given an m x n matrix board, representing the current state of a crossword puzzle. The crossword contains lowercase English letters (from solved words), ' ' to represent any empty cells, and '#' to represent any blocked cells.
# A word can be placed horizontally (left to right or right to left) or vertically (top to bottom or bottom to top) in the board if:
# It does not occupy a cell containing the character '#'.
# The cell each letter is placed in must either be ' ' (empty) or match the letter already on the board.
# There must not be any empty cells ' ' or other lowercase letters directly left or right of the word if the word was placed horizontally.
# There must not be any empty cells ' ' or other lowercase letters directly above or below the word if the word was placed vertically.
# Given a string word, return true if word can be placed in board, or false otherwise.
from typing import List


class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                left_to_right = (j == 0 or self.board[i][j - 1] == "#") and self.check(
                    i, j, 0, 1, word
                )
                right_to_left = (
                    j == len(self.board[0]) - 1 or self.board[i][j + 1] == "#"
                ) and self.check(i, j, 0, -1, word)
                up_to_down = (i == 0 or self.board[i - 1][j] == "#") and self.check(
                    i, j, 1, 0, word
                )
                down_to_up = (
                    i == len(self.board) - 1 or self.board[i + 1][j] == "#"
                ) and self.check(i, j, -1, 0, word)
                if left_to_right or right_to_left or up_to_down or down_to_up:
                    return True
        return False

    def check(self, i, j, a, b, word):
        x = i + a * len(word)
        y = j + b * len(word)
        if (
            (0 <= x < len(self.board))
            and (0 <= y < len(self.board[0]))
            and (self.board[x][y] != "#")
        ):
            return False
        for c in word:
            if (
                i < 0
                or i >= len(self.board)
                or j < 0
                or j >= len(self.board[0])
                or (self.board[i][j] != " " and self.board[i][j] != c)
            ):
                return False
            i += a
            j += b
        return True
