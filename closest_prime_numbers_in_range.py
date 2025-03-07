# Given two positive integers left and right, find the two integers num1 and num2 such that:
# left <= num1 < num2 <= right .
# Both num1 and num2 are prime numbers.
# num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
# Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].
from typing import List
from math import inf


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if left == 1:
            left += 1
        if right <= left:
            return [-1, -1]
        num_dict = {num: 0 for num in range(min(left, 2), right+1)}
        p = 2
        while True:
            p2 = p * p
            if p2 > right:
                break
            q = p + p
            while q <= right:
                num_dict[q] = 1
                q += p
            q0 = p + 1
            p = None
            while q0 <= p2:
                if num_dict[q0] == 0:
                    p = q0
                    break
                else:
                    q0 += 1
            if p is None:
                break
        nums = [num for num in num_dict if (num_dict[num] == 0) and (num >= left)]
        if len(nums) == 1:
            return [-1, -1]
        nums.sort()
        diff = inf
        res = [-1, -1]
        for i in range(1, len(nums)):
            cur_diff = nums[i] - nums[i-1] 
            if diff > cur_diff:
                res = [nums[i-1], nums[i]]
                diff = min(cur_diff, diff)                
        return res
