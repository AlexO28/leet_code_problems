# Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        nums_odd = [num for num in nums if num % 2 == 1]
        nums_even = [num for num in nums if num % 2 == 0]
        nums_even.extend(nums_odd)
        return nums_even
