# Alice and Bob take turns playing a game, with Alice starting first.
# Initially, there are n stones in a pile. On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.
# Also, if a player cannot make a move, he/she loses the game.
# Given a positive integer n, return true if and only if Alice wins the game otherwise return false, assuming both players play optimally.
from functools import cache


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        return self.canWin(n)

    @cache
    def canWin(self, remaining_stones):
        if remaining_stones == 0:
            return False
        else:
            square_root = 1
            while True:
                stones_to_remove = square_root * square_root
                delta = remaining_stones - stones_to_remove
                if delta < 0:
                    break
                else:
                    if not self.canWin(delta):
                        return True
                square_root += 1
            return False
