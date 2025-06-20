# Given a list of words, list of  single letters (might be repeating) and score of every character.
# Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).
# It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.
from typing import List
from collections import Counter


class Solution:
    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        available_letters = Counter(letters)
        max_score = 0
        for i in range(1 << len(words)):
            cur_count = Counter(
                "".join(words[j] for j in range(len(words)) if (i >> j) & 1)
            )
            if all(
                cur_count[letter] <= available_letters[letter] for letter in cur_count
            ):
                max_score = max(
                    max_score,
                    sum(
                        cur_count[letter] * score[ord(letter) - ord("a")]
                        for letter in cur_count
                    ),
                )
        return max_score
