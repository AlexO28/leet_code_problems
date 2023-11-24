# There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:
# In each step, you will choose any 3 piles of coins (not necessarily consecutive).
# Of your choice, Alice will pick the pile with the maximum number of coins.
# You will pick the next pile with the maximum number of coins.
# Your friend Bob will pick the last pile.
# Repeat until there are no more piles of coins.
# Given an array of integers piles where piles[i] is the number of coins in the ith pile.
# Return the maximum number of coins that you can have.

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        bobs_pos = 0
        my_pos = len(piles)-2
        res = 0
        while my_pos >= bobs_pos:
            res += piles[my_pos]
            my_pos -= 2
            bobs_pos += 1
        return res
   
