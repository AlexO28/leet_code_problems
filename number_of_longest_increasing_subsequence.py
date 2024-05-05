# Given an integer array nums, return the number of longest increasing subsequences.
# Notice that the sequence has to be strictly increasing.
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        dp_1 = [1]*len(nums)
        dp_2 = [1]*len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    val = dp_1[j] + 1 
                    if val > dp_1[i]:
                        dp_1[i] = val
                        dp_2[i] = dp_2[j]
                    elif val == dp_1[i]:
                        dp_2[i] += dp_2[j]
        max_len = max([x for x in dp_1])
        count = 0
        for val1, val2 in zip(dp_1, dp_2):
            if val1 == max_len:
                count += val2
        return count
