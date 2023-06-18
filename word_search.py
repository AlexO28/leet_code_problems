# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

MAX_DEPTH = 15

def check_cell(depth, word, i, j, marks, board):
    if depth >= MAX_DEPTH:
        return True, marks
    if depth >= len(word):
        return True, marks
    if i + 1 < len(board):
        if (board[i + 1][j] == word[depth]) and ([i + 1, j] not in marks):
            marks.append([i + 1, j])
            res, marks = check_cell(depth + 1, word, i + 1, j, marks, board)
            if res:
                return True, marks
            marks = [mark for mark in marks if mark != [i + 1, j]]
    if i - 1 >= 0:
        if (board[i - 1][j] == word[depth]) and ([i - 1, j] not in marks):
            marks.append([i - 1, j])
            res, marks = check_cell(depth + 1, word, i - 1, j, marks, board)
            if res:
                return True, marks
            marks = [mark for mark in marks if mark != [i - 1, j]]
    if j + 1 < len(board[0]):
        if (board[i][j + 1] == word[depth]) and ([i, j + 1] not in marks):
            marks.append([i, j + 1])
            res, marks = check_cell(depth + 1, word, i, j + 1, marks, board)
            if res:
                return True, marks
            marks = [mark for mark in marks if mark != [i, j + 1]]
    if j - 1 >= 0:
        if (board[i][j - 1] == word[depth]) and ([i, j - 1] not in marks):
            marks.append([i, j - 1])
            res, marks = check_cell(depth + 1, word, i,  j - 1, marks, board)
            if res:
                return True, marks
            marks = [mark for mark in marks if mark != [i, j - 1]]
    return False, marks

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        unique_letters = list(set(list(word)))
        num_found = 0
        for letter in unique_letters:
            found_letter = False
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == letter:
                        found_letter = True
                        num_found += 1
                    if found_letter:
                        break
                if found_letter:
                    break
        if num_found != len(unique_letters):
            return False
        marks = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if len(word) == 1:
                        return True
                    else:
                        marks.append([i, j])
                        res, marks = check_cell(1, word, i, j, marks, board)
                        if res:
                            return True
                        marks = [mark for mark in marks if mark != [i, j]]
        return False
