# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        max_len = 0
        num_dict = {}
        diff = 0
        num_dict[diff] = -1 
        for j in range(len(nums)):
            if nums[j] == 1:
                diff += 1
            else:
                diff -= 1
            if diff in num_dict:
                max_len = max(max_len, j - num_dict[diff])
            else:
                num_dict[diff] = j
        return max_len
