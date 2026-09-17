# Alice is a caretaker of n gardens and she wants to plant flowers to maximize the total beauty of all her gardens.
# You are given a 0-indexed integer array flowers of size n, where flowers[i] is the number of flowers already planted in the ith garden. Flowers that are already planted cannot be removed. You are then given another integer newFlowers, which is the maximum number of flowers that Alice can additionally plant. You are also given the integers target, full, and partial.
# A garden is considered complete if it has at least target flowers. The total beauty of the gardens is then determined as the sum of the following:
# The number of complete gardens multiplied by full.
# The minimum number of flowers in any of the incomplete gardens multiplied by partial. If there are no incomplete gardens, then this value will be 0.
# Return the maximum total beauty that Alice can obtain after planting at most newFlowers flowers.
from typing import List
from itertools import accumulate
from bisect import bisect_left


class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        flowers.sort()
        s = list(accumulate(flowers, initial=0))
        ans = 0
        i = len(flowers) - bisect_left(flowers, target)
        for x in range(i, len(flowers) + 1):
            if x != 0:
                newFlowers -= max(target - flowers[len(flowers) - x], 0)
            if newFlowers < 0:
                break
            l = 0 
            r = len(flowers) - x - 1
            while l < r:
                mid = (l + r + 1) >> 1
                if flowers[mid] * (mid + 1) - s[mid + 1] <= newFlowers:
                    l = mid
                else:
                    r = mid - 1
            y = 0
            if r != -1:
                cost = flowers[l] * (l + 1) - s[l + 1]
                y = min(flowers[l] + (newFlowers - cost) // (l + 1), target - 1)
            ans = max(ans, x * full + y * partial)
        return ans
