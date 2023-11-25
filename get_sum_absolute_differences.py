# You are given an integer array nums sorted in non-decreasing order.
# Build and return an integer array result with the same length as nums such that result[i] is equal to the summation of absolute differences between nums[i] and all the other elements in the array.
# In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix_sum = 0
        suffix_sum = sum(nums[1:])
        res = []
        for i in range(len(nums)):
            res.append(nums[i]*(2*i-len(nums)+1) - prefix_sum + suffix_sum)
            prefix_sum += nums[i]
            if i < len(nums) - 1:
                suffix_sum -= nums[i+1]
        return res
