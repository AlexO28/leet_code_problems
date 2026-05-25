# There is a tournament where n players are participating. The players are standing in a single row and are numbered from 1 to n based on their initial standing position (player 1 is the first player in the row, player 2 is the second player in the row, etc.).
# The tournament consists of multiple rounds (starting from round number 1). In each round, the ith player from the front of the row competes against the ith player from the end of the row, and the winner advances to the next round. When the number of players is odd for the current round, the player in the middle automatically advances to the next round.
# For example, if the row consists of players 1, 2, 4, 6, 7
# Player 1 competes against player 7.
# Player 2 competes against player 6.
# Player 4 automatically advances to the next round.
# After each round is over, the winners are lined back up in the row based on the original ordering assigned to them initially (ascending order).
# The players numbered firstPlayer and secondPlayer are the best in the tournament. They can win against any other player before they compete against each other. If any two other players compete against each other, either of them might win, and thus you may choose the outcome of this round.
# Given the integers n, firstPlayer, and secondPlayer, return an integer array containing two values, the earliest possible round number and the latest possible round number in which these two players will compete against each other, respectively.
from typing import List
from functools import cache
from math import inf


class Solution:
    def earliestAndLatest(
        self, n: int, firstPlayer: int, secondPlayer: int
    ) -> List[int]:
        return self.search(firstPlayer - 1, secondPlayer - 1, n)

    @cache
    def search(self, l, r, n):
        if l + r == n - 1:
            return [1, 1]
        res = [inf, -inf]
        m = n >> 1
        for i in range(1 << m):
            win = [False] * n
            for j in range(m):
                if i >> j & 1:
                    win[j] = True
                else:
                    win[n - 1 - j] = True
            if n & 1:
                win[m] = True
            win[n - 1 - l] = False
            win[n - 1 - r] = False
            win[l] = True
            win[r] = True
            a = 0
            b = 0
            c = 0
            for j in range(n):
                if j == l:
                    a = c
                if j == r:
                    b = c
                if win[j]:
                    c += 1
            x, y = self.search(a, b, c)
            res[0] = min(res[0], x + 1)
            res[1] = max(res[1], y + 1)
        return res
