# Given an integer array nums, your goal is to make all elements in nums equal. To complete one operation, follow these steps:
# Find the largest value in nums. Let its index be i (0-indexed) and its value be largest. If there are multiple elements with the largest value, pick the smallest i.
# Find the next largest value in nums strictly smaller than largest. Let its value be nextLargest.
# Reduce nums[i] to nextLargest.
# Return the number of operations to make all elements in nums equal.

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        nums_dict = {}
        for num in nums:
            if num in nums_dict.keys():
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1
        nums_keys = list(nums_dict.keys())
        nums_keys.sort()
        if len(nums_keys) == 1:
            return 0
        count = 0
        min_key = nums_keys[0]
        for j in range(len(nums_keys)):
            count += j*nums_dict[nums_keys[j]]
        return count
