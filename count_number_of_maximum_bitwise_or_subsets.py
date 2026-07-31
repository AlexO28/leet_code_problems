# Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.
# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.
# The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).
from typing import List


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        max_num = 2 ** len(nums)
        res = []
        for num in range(max_num):
            num_str = bin(num)[2:]
            delta = len(nums) - len(num_str)
            if delta > 0:
                num_str = "0" * delta + num_str
            data = []
            for i in range(len(num_str)):
                if num_str[i] == "1":
                    data.append(nums[i])
            if len(data) == 1:
                res.append(data[0])
            elif len(data) > 1:
                res.append(self.calculate(data))
        max_val = max(res)
        return res.count(max_val)

    def calculate(self, data):
        cur_res = data[0]
        for i in range(1, len(data)):
            cur_res |= data[i]
        return cur_res
