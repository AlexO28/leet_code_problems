# We are playing the Guess Game. The game is as follows:
# I pick a number from 1 to n. You have to guess which number I picked.
# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
# You call a pre-defined API int guess(int num), which returns three possible results:
# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
import numpy as np


class Solution:
    def guessNumber(self, n: int) -> int:
        if guess(1) == 0:
            return 1
        if guess(n) == 0:
            return n
        return self.findNumber(1, n)

    def findNumber(self, a, b):
        if b-a <= 2:
            mid = b-1
        else:
            mid = int(np.ceil((b + a)/2))
        the_guess = guess(mid)
        if the_guess == 0:
            return mid
        elif the_guess > 0:
            return self.findNumber(mid, b)
        else:
            return self.findNumber(a, mid)
