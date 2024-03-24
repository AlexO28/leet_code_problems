# Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.
# Return the shortest such subarray and output its length.
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        nums_sorted = sorted(nums)
        first_index = -1
        cur_index = -1
        for j in range(len(nums)):
            if nums[j] != nums_sorted[j]:
                cur_index = j
                if first_index < 0:
                    first_index = j
        if first_index < 0:
            return 0
        else:
            return cur_index - first_index + 1
 
