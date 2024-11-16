# Given an integer array nums, partition it into two (contiguous) subarrays left and right so that:
# Every element in left is less than or equal to every element in right.
# left and right are non-empty.
# left has the smallest possible size.
# Return the length of left after such a partitioning.
# Test cases are generated such that partitioning exists.
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return 1
        start = 0
        possible_max_val = nums[start]
        while start < len(nums):
            max_val = possible_max_val
            found = False
            for j in range(start+1, len(nums)):
                if nums[j] < max_val:
                    found = True
                    start = j
                    break
                else:
                    possible_max_val = max(possible_max_val, nums[j])
            if not found:
                return start + 1
