# You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:
# Choose the pile with the maximum number of gifts.
# If there is more than one pile with the maximum number of gifts, choose any.
# Leave behind the floor of the square root of the number of gifts in the pile. Take the rest of the gifts.
# Return the number of gifts remaining after k seconds.
import bisect
from typing import List
import math


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts.sort()
        for j in range(k):
            elem = math.floor(math.sqrt(gifts.pop(len(gifts)-1)))
            bisect.insort(gifts, elem)
        return sum(gifts)
