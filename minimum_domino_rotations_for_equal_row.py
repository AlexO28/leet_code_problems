# In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
# We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.
# Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.
# If it cannot be done, return -1
from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        val0 = tops[0]
        val1 = bottoms[0]
        freqs_1 = []
        freqs_2 = []
        for i in range(len(tops)):
            if (tops[i] == val0) or (bottoms[i] == val0):
                freqs_1.append(1)
            else:
                freqs_1.append(0)
            if (tops[i] == val1) or (bottoms[i] == val1):
                freqs_2.append(1)
            else:
                freqs_2.append(0)
        summa_1 = sum(freqs_1)
        summa_2 = sum(freqs_2)
        if summa_1 > summa_2:
            val = val0
        else:
            val = val1
        top = 0
        bottom = 0
        for i in range(len(tops)):
            if (tops[i] == val) and (bottoms[i] == val):
                continue
            elif tops[i] == val:
                top += 1
            elif bottoms[i] == val:
                bottom += 1
            else:
                return -1
        return min(top, bottom)
