# Alice and Bob take turns playing a game, with Alice starting first.
# There are n stones arranged in a row. On each player's turn, they can remove either the leftmost stone or the rightmost stone from the row and receive points equal to the sum of the remaining stones' values in the row. The winner is the one with the higher score when there are no stones left to remove.
# Bob found that he will always lose this game (poor Bob, he always loses), so he decided to minimize the score's difference. Alice's goal is to maximize the difference in the score.
# Given an array of integers stones where stones[i] represents the value of the ith stone from the left, return the difference in Alice and Bob's score if they both play optimally.
from typing import List
from functools import cache
from itertools import accumulate


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        self.s = list(accumulate(stones, initial=0))
        res = self.search(0, len(stones) - 1)
        self.search.cache_clear()
        return res

    @cache
    def search(self, i, j):
        if i > j:
            return 0
        return max(
            self.s[j + 1] - self.s[i + 1] - self.search(i + 1, j),
            self.s[j] - self.s[i] - self.search(i, j - 1),
        )
