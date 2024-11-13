# You are given an integer array nums and an integer k.
# For each index i where 0 <= i < nums.length, change nums[i] to be either nums[i] + k or nums[i] - k.
# The score of nums is the difference between the maximum and minimum elements in nums.
# Return the minimum score of nums after changing the values at each index.
class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        nums.sort()
        smallest_range = nums[-1] - nums[0]
        for j in range(1, len(nums)):
            smallest_range = min(smallest_range, max(nums[j-1] + k, nums[-1] - k) - min(nums[0] + k, nums[j] - k))
        return smallest_range
