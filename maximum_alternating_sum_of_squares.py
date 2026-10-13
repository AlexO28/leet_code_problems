# You are given an integer array nums. You may rearrange the elements in any order.
# The alternating score of an array arr is defined as:
# score = arr[0]2 - arr[1]2 + arr[2]2 - arr[3]2 + ...
# Return an integer denoting the maximum possible alternating score of nums after rearranging its elements.
from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = [abs(num) for num in nums]
        if len(nums) == 1:
            return nums[0] * nums[0]
        nums.sort()
        first = len(nums) - 1
        second = 0
        summa = 0
        add_first = True
        while first >= second:
            if add_first:
                summa += nums[first] * nums[first]
                first -= 1
                add_first = False
            else:
                summa -= nums[second] * nums[second]
                second += 1
                add_first = True
        return summa
