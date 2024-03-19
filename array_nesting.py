# You are given an integer array nums of length n where nums is a permutation of the numbers in the range [0, n - 1].
# You should build a set s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ... } subjected to the following rule:
# The first element in s[k] starts with the selection of the element nums[k] of index = k.
# The next element in s[k] should be nums[nums[k]], and then nums[nums[nums[k]]], and so on.
# We stop adding right before a duplicate element occurs in s[k].
# Return the longest length of a set s[k].
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        max_nesting_size = 0
        for i in range(len(nums)):
            current_size = 0
            while nums[i] != -1:
                next_index = nums[i]
                nums[i] = -1
                i = next_index
                current_size += 1
            max_nesting_size = max(max_nesting_size, current_size)
        return max_nesting_size
