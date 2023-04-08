# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(len(nums)):
            num = nums[i]
            if ~(num in num_dict.keys()):
                num_dict[num] = i
        for i in range(len(nums)):
            if (target - nums[i]) in num_dict.keys():
                if i != num_dict[target - nums[i]]:
                    return [i, num_dict[target - nums[i]]]
