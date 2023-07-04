# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        max_len = 0
        num_prev = nums[0] - 1
        count = 0
        for num in nums:
            if num - num_prev == 1:
                count += 1
            elif num - num_prev > 1:
                max_len = max(max_len, count)
                count = 1
            num_prev = num
        max_len = max(max_len, count)
        return max_len
