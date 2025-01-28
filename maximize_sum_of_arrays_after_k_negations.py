# Given an integer array nums and an integer k, modify the array in the following way:
# choose an index i and replace nums[i] with -nums[i].
# You should apply this process exactly k times. You may choose the same index i multiple times.
# Return the largest possible sum of the array after modifying it in this way.
from typing import List


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        num_dict = {}
        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        for num in range(-100, 0):
            if num in num_dict:
                num_negations = min(num_dict[num], k)
                num_dict[num] -= num_negations
                neg = -num
                if neg in num_dict:
                    num_dict[neg] += num_negations
                else:
                    num_dict[neg] = num_negations
                k -= num_negations
                if k == 0:
                    break
        if (k % 2 == 1) and (0 not in num_dict):
            for num in range(1, 101):
                if num in num_dict:
                    num_dict[num] -= 1
                    neg = -num
                    if neg in num_dict:
                        num_dict[neg] += 1
                    else:
                        num_dict[neg] = 1
                    break
        return sum(num*num_dict[num] for num in num_dict)
