# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        else:
            res = [nums[0]]
            cur_sum = nums[0]
            for j in range(1, len(nums)):
                cur_sum += nums[j]
                res.append(cur_sum)
            return res
