# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        num_prev = nums[0]-1
        for num in nums:
            if num == num_prev:
                return True
            num_prev = num
        return False
