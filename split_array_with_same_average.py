# You are given an integer array nums.
# You should move each element of nums into one of the two arrays A and B such that A and B are non-empty, and average(A) == average(B).
# Return true if it is possible to achieve that and false otherwise.
class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return False
        total_sum = sum(nums)
        nums = [num*len(nums)-total_sum for num in nums]
        half_num_elements = len(nums) >> 1
        seen_sums_first_half = set()
        for bitmask in range(1, 1 << half_num_elements):
            subset_sum = sum([nums[j] for j in range(half_num_elements) if bitmask >> j & 1])
            if subset_sum == 0:
                return True
            seen_sums_first_half.add(subset_sum)
        for bitmask in range(1, 1 << (len(nums) - half_num_elements)):
            subset_sum = sum(value for j, value in enumerate(nums[half_num_elements:]) if bitmask >> j & 1)
            if (subset_sum == 0) or  ((bitmask != (1 << (len(nums) - half_num_elements)) - 1) and (-subset_sum in seen_sums_first_half)):
                return True
        return False
