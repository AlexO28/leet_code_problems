# You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.
# Notice that x does not have to be an element in nums.
# Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            if nums[0] > 0:
                return 1
            else:
                return -1
        res = [0]*1000
        for num in nums:
            if num > 0:
                for j in range(num):
                    res[j] += 1
        for j in range(1000):
            if res[j] == j+1:
                return j+1
        return -1
