# On an alphabet board, we start at position (0, 0), corresponding to character board[0][0].
# Here, board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"], as shown in the diagram below.
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        self.letters = {"a": [0, 0], "b": [0, 1], "c": [0, 2], "d": [0, 3], "e": [0, 4],
                        "f": [1, 0], "g": [1, 1], "h": [1, 2], "i": [1, 3], "j": [1, 4],
                        "k": [2, 0], "l": [2, 1], "m": [2, 2], "n": [2, 3], "o": [2, 4],
                        "p": [3, 0], "q": [3, 1], "r": [3, 2], "s": [3, 3], "t": [3, 4],
                        "u": [4, 0], "v": [4, 1], "w": [4, 2], "x": [4, 3], "y": [4, 4],
                        "z": [5, 0]}
        self.path = []
        letter_start = "a"
        for letter in list(target):
            self.buildPathBetweenLetters(letter_start, letter)
            letter_start = letter
        return "".join(self.path)

    def buildPathBetweenLetters(self, letter1, letter2):
        row1, col1 = self.letters[letter1]
        row2, col2 = self.letters[letter2]
        row_diff = row2 - row1
        col_diff = col2 - col1
        if letter1 == "z":
            if row_diff > 0:
                self.path.extend("D" * (row_diff))
            elif row_diff < 0:
                self.path.extend("U" * (-row_diff))
            if col_diff > 0:
                self.path.extend("R" * (col_diff))
            elif col_diff < 0:
                self.path.extend("L" * (-col_diff))
        else:
            if col_diff > 0:
                self.path.extend("R" * (col_diff))
            elif col_diff < 0:
                self.path.extend("L" * (-col_diff))
            if row_diff > 0:
                self.path.extend("D" * (row_diff))
            elif row_diff < 0:
                self.path.extend("U" * (-row_diff))
        self.path.append("!")
