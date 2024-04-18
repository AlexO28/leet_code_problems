# Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        max_len = 1
        start = 1
        cur_len = 1
        for start in range(1, len(nums)):
            if nums[start] > nums[start-1]:
                cur_len += 1
            else:
                max_len = max(max_len, cur_len)
                cur_len = 1
        return max(max_len, cur_len)
 
