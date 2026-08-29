# You are given an array nums of positive integers. In one operation, you can choose any number from nums and reduce it to exactly half the number. (Note that you may choose this reduced number in future operations.)
# Return the minimum number of operations to reduce the sum of nums by at least half.
from typing import List
from sortedcontainers import SortedList


class Solution:
    def halveArray(self, nums: List[int]) -> int:
        nums = SortedList(nums)
        cur_sum = sum(nums)
        min_operations = 0
        target_sum = cur_sum / 2
        while cur_sum > target_sum:
            elem = nums.pop() / 2
            cur_sum -= elem
            nums.add(elem)
            min_operations += 1
        return min_operations
