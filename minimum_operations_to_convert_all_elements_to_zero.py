# You are given an array nums of size n, consisting of non-negative integers. Your task is to apply some (possibly zero) operations on the array so that all elements become 0.
# In one operation, you can select a subarray [i, j] (where 0 <= i <= j < n) and set all occurrences of the minimum non-negative integer in that subarray to 0.
# Return the minimum number of operations required to make all elements in the array 0.
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            if nums[0] == 0:
                return 0
            else:
                return 1
        else:
            stk = []
            ans = 0
            for x in nums:
                while stk and stk[-1] > x:
                    ans += 1
                    stk.pop()
                if x and (not stk or stk[-1] != x):
                    stk.append(x)
            ans += len(stk)
            return ans
