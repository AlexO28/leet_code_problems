# You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].
# Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.
from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return -1
        num_dict = {}
        for num in nums:
            summa = sum([int(elem) for elem in list(str(num))])
            if summa in num_dict:
                num_dict[summa].append(num)
            else:
                num_dict[summa] = [num]
        max_val = -1
        for num in num_dict:
            if len(num_dict[num]) > 1:
                num_dict[num].sort()
                max_val = max(max_val, num_dict[num][-1] + num_dict[num][-2])
        return max_val
