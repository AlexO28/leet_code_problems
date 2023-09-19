# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        number_of_zeros = 0
        while True:
            if index >= len(nums):
                break
            if nums[index] == 0:
                del nums[index]
                number_of_zeros += 1
            else:
                index += 1
        if number_of_zeros > 0:
            nums.extend([0]*(number_of_zeros))
        
