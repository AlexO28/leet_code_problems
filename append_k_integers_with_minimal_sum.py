# You are given an integer array nums and an integer k. Append k unique positive integers that do not appear in nums to nums such that the resulting total sum is minimum.
# Return the sum of the k integers appended to nums.
from typing import List


class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        res = k * (k + 1) // 2
        nums = sorted(set(nums))
        next_num = k + 1
        for num in nums:
            if num < next_num:
                res -= num
                res += next_num
                next_num += 1
        return res
