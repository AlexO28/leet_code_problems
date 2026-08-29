# You are given a 0-indexed integer array candies. Each element in the array denotes a pile of candies of size candies[i]. You can divide each pile into any number of sub piles, but you cannot merge two piles together.
# You are also given an integer k. You should allocate piles of candies to k children such that each child gets the same number of candies. Each child can be allocated candies from only one pile of candies and some piles of candies may go unused.
# Return the maximum number of candies each child can get.
from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        self.candies = candies
        start = 0
        end = sum(candies)
        while end - start > 1:
            mid = (end + start) // 2
            if self.divide(k, mid):
                start = mid
            else:
                end = mid
        if self.divide(k, end):
            return end
        else:
            return start

    def divide(self, k, num_candies):
        if num_candies == 0:
            return True
        max_num = 0
        for group in self.candies:
            max_num += group // num_candies
        return max_num >= k
        
