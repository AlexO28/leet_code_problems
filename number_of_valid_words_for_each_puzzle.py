# With respect to a given puzzle string, a word is valid if both the following conditions are satisfied:
# word contains the first letter of puzzle.
# For each letter in word, that letter is in puzzle.
# For example, if the puzzle is "abcdefg", then valid words are "faced", "cabbage", and "baggage", while
# invalid words are "beefed" (does not include 'a') and "based" (includes 's' which is not in the puzzle).
# Return an array answer, where answer[i] is the number of words in the given word list words that is valid with respect to the puzzle puzzles[i].
from typing import List
from collections import Counter


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        bitmask_counter = Counter()
        a_code = ord('a')
        for word in words:
            bitmask = 0
            for char in word:
                bitmask |= 1 << (ord(char) - a_code)
            bitmask_counter[bitmask] += 1
        results = []
        for puzzle in puzzles:
            puzzle_bitmask = 0
            for char in puzzle:
                puzzle_bitmask |= 1 << (ord(char) - a_code)          
            valid_word_count = 0
            first_char_bit = ord(puzzle[0]) - a_code
            submask = puzzle_bitmask
            while submask:
                if submask >> first_char_bit & 1:
                    valid_word_count += bitmask_counter[submask]
                submask = (submask - 1) & puzzle_bitmask          
            results.append(valid_word_count)
        return results
