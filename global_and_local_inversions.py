# You are given an integer array nums of length n which represents a permutation of all the integers in the range [0, n - 1].
# The number of global inversions is the number of the different pairs (i, j) where:
# 0 <= i < j < n
# nums[i] > nums[j]
# The number of local inversions is the number of indices i where:
# 0 <= i < n - 1
# nums[i] > nums[i + 1]
# Return true if the number of global inversions is equal to the number of local inversions.
class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True
        max_num = nums[0]
        for j in range(2, len(nums)):
            if nums[j] < max_num:
                return False
            max_num = max(max_num, nums[j-1])
        return True
