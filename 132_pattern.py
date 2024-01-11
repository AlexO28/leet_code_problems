# Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
# Return true if there is a 132 pattern in nums, otherwise, return false.
import math

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        last = -math.inf
        stack = []
        for num in nums[::-1]:
            if num < last:
                return True
            while stack and stack[-1] < num:
                last = stack.pop()
            stack.append(num)
        return False
