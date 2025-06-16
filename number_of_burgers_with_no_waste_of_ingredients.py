# Given two integers tomatoSlices and cheeseSlices. The ingredients of different burgers are as follows:
# Jumbo Burger: 4 tomato slices and 1 cheese slice.
# Small Burger: 2 Tomato slices and 1 cheese slice.
# Return [total_jumbo, total_small] so that the number of remaining tomatoSlices equal to 0 and the number of remaining cheeseSlices equal to 0. If it is not possible to make the remaining tomatoSlices and cheeseSlices equal to 0 return [].
from typing import List


class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        x = tomatoSlices/2 - cheeseSlices
        y = 2*cheeseSlices - tomatoSlices/2
        if (x >= 0) and (y >= 0) and (x.is_integer()) and (y.is_integer()):
            return [int(x), int(y)]
        else:
            return []
