# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k >= len(nums):
            k = k % len(nums)
        if k > 0:
            new_arr = nums[(len(nums)-k):len(nums)]
            new_arr.extend(nums[:(len(nums)-k)])
            for j in range(len(nums)):
                nums[j] = new_arr[j]
