# An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.
# For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
# Given an integer array nums, return the number of arithmetic subarrays of nums.
# A subarray is a contiguous subsequence of the array.
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 0
        counter = 0
        for j in range(len(nums)-2):
            diff = nums[j+1] - nums[j]
            number_of_hits = 0
            for i in range(j+1, len(nums)-1):
                if nums[i+1] - nums[i] == diff:
                    number_of_hits += 1
                else:
                    break
            if number_of_hits > 0:
                counter += number_of_hits
        return counter
