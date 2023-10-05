# Given an integer array nums, return the length of the longest strictly increasing subsequence.


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        lis = [1]
        max_val = 1
        for j in range(1, len(nums)):
            candidate = 1
            for i in range(len(lis)):
                if nums[j] > nums[i]:
                    candidate = max(candidate, lis[i] + 1)
            max_val = max(max_val, candidate)
            lis.append(candidate)
        return max_val
