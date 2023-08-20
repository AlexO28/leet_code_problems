# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

import functools


class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def compare(x, y):
            num1 = int(x + y)
            num2 = int(y + x)
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
            else:
                return 0

        nums = [str(num) for num in nums]
        nums.sort(key=functools.cmp_to_key(compare), reverse = True)
        line = ''.join(nums)
        res = ""
        skip = True
        for elem in line:
            if not skip:
                res += elem
            elif elem != "0":
                res += elem
                skip = False
        if len(res) == 0:
            return "0"
        return res
