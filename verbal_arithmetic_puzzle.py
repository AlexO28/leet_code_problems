# Given an equation, represented by words on the left side and the result on the right side.
# You need to check if the equation is solvable under the following rules:
# Each character is decoded as one digit (0 - 9).
# No two characters can map to the same digit.
# Each words[i] and result are decoded as one number without leading zeros.
# Sum of numbers on the left side (words) will equal to the number on the right side (result).
# Return true if the equation is solvable, otherwise return false.
from typing import List


class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        num_equal = 0
        num_not_equal = 0
        max_len = 0
        for word in words:
            if word == result:
                num_equal += 1
            else:
                num_not_equal += 1
                max_len = max(max_len, len(word))
        if num_equal > 0:
            if (num_not_equal == 1) and (max_len == 1):
                return True
            if num_not_equal == 0:
                return len(result) == 1
            return False
        words.append(result)
        self.rows = len(words)
        self.cols = max(map(len, words))
        self.letterToDigit = {}
        self.usedDigit = [False] * 10
        self.words = words
        return self.search(0, 0, 0)

    def search(self, row, col, summa):
        if col == self.cols:
            return summa == 0
        if row == self.rows:
            main_part, remainder = divmod(summa, 10)
            return remainder == 0 and self.search(0, col + 1, main_part)
        word = self.words[row]
        if col >= len(word):
            return self.search(row + 1, col, summa)
        letter = word[~col]
        if row == self.rows - 1:
            sign = -1
        else:
            sign = 1
        if letter in self.letterToDigit and (
            self.letterToDigit[letter] > 0 or col < len(word) - 1
        ):
            return self.search(row + 1, col, summa + sign * self.letterToDigit[letter])
        for digit, used in enumerate(self.usedDigit):
            if not used and (digit > 0 or col < len(word) - 1):
                self.letterToDigit[letter] = digit
                self.usedDigit[digit] = True
                if self.search(row + 1, col, summa + sign * digit):
                    return True
                self.usedDigit[digit] = False
                if letter in self.letterToDigit:
                    del self.letterToDigit[letter]
        return False
