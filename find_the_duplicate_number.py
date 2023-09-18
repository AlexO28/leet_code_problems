# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for j in range(len(nums)):
            if nums[j] < j + 1:
                return nums[j]
        return nums[-1]
