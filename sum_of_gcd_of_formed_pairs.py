# You are given an integer array nums of length n.
# Construct an array prefixGcd where for each index i:
# Let mxi = max(nums[0], nums[1], ..., nums[i]).
# prefixGcd[i] = gcd(nums[i], mxi).
# After constructing prefixGcd:
# Sort prefixGcd in non-decreasing order.
# Form pairs by taking the smallest unpaired element and the largest unpaired element.
# Repeat this process until no more pairs can be formed.
# For each formed pair, compute the gcd of the two elements.
# If n is odd, the middle element in the prefixGcd array remains unpaired and should be ignored.
# Return an integer denoting the sum of the GCD values of all formed pairs.
from typing import List
from math import gcd


class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        else:
            prefixGcds = []
            curMax = nums[0]
            for num in nums:
                curMax = max(curMax, num)
                prefixGcds.append(gcd(num, curMax))
            prefixGcds.sort()
            summa = 0
            for j in range(len(prefixGcds) // 2):
                summa += gcd(prefixGcds[j], prefixGcds[len(prefixGcds) - j - 1])
            return summa
