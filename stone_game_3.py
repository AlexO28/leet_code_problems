# Alice and Bob continue their games with piles of stones. There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.
# Alice and Bob take turns, with Alice starting first. On each player's turn, that player can take 1, 2, or 3 stones from the first remaining stones in the row.
# The score of each player is the sum of the values of the stones taken. The score of each player is 0 initially.
# The objective of the game is to end with the highest score, and the winner is the player with the highest score and there could be a tie. The game continues until all the stones have been taken.
# Assume Alice and Bob play optimally.
# Return "Alice" if Alice will win, "Bob" if Bob will win, or "Tie" if they will end the game with the same score.
from typing import List
from functools import cache
from math import inf


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        self.stoneValue = stoneValue
        aliceScoreDiff = self.search(0)
        if aliceScoreDiff > 0:
            return "Alice"
        elif aliceScoreDiff == 0:
            return "Tie"
        else:
            return "Bob"

    @cache
    def search(self, index):
        if index >= len(self.stoneValue):
            return 0
        max_score_diff = -inf
        current_sum = 0
        for num_stones in range(3):
            if index + num_stones >= len(self.stoneValue):
                break
            current_sum += self.stoneValue[index + num_stones]
            score_diff = current_sum - self.search(index + num_stones + 1)
            max_score_diff = max(max_score_diff, score_diff)
        return max_score_diff
