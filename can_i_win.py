# In the "100 game" two players take turns adding, to a running total, any integer from 1 to 10. The player who first causes the running total to reach or exceed 100 wins.
# What if we change the game so that players cannot re-use integers?
# For example, two players might take turns drawing from a common pool of numbers from 1 to 15 without replacement until they reach a total >= 100.
# Given two integers maxChoosableInteger and desiredTotal, return true if the first player to move can force a win, otherwise, return false. Assume both players play optimally.
from functools import cache

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        sum_of_integers = (1 + maxChoosableInteger) * maxChoosableInteger // 2
        if sum_of_integers < desiredTotal:
            return False
        return self.can_win_game(0, 0, maxChoosableInteger, desiredTotal)

    @cache
    def can_win_game(self, state, current_total, maxChoosableInteger, desiredTotal):
        for integer in range(1, maxChoosableInteger + 1):
            if (state >> integer) & 1:
                continue
            if current_total + integer >= desiredTotal or not self.can_win_game(state | (1 << integer), current_total + integer, maxChoosableInteger, desiredTotal):
                return True
        return False
