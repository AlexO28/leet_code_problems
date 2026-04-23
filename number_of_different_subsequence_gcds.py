# You are given an array nums that consists of positive integers.
# The GCD of a sequence of numbers is defined as the greatest integer that divides all the numbers in the sequence evenly.
# For example, the GCD of the sequence [4,6,16] is 2.
# A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.
# For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
# Return the number of different GCDs among all non-empty subsequences of nums.
from typing import List
from math import gcd


class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        mx = max(nums) + 1
        vis = set(nums)
        ans = 0
        for x in range(1, mx):
            g = 0
            for y in range(x, mx, x):
                if y in vis:
                    g = gcd(g, y)
                    if g == x:
                        ans += 1
                        break
        return ans
