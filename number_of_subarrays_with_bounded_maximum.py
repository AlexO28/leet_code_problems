# Given an integer array nums and two integers left and right, return the number of contiguous non-empty subarrays such that the value of the maximum array element in that subarray is in the range [left, right].
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        self.nums = nums
        return self.count_subarrays_with_max_less_than_boundary(right) - self.count_subarrays_with_max_less_than_boundary(left-1)

    def count_subarrays_with_max_less_than_boundary(self, boundary):
        count = 0
        temp_count = 0
        for num in self.nums:
            if num > boundary:
                temp_count = 0
            else:
                temp_count += 1
            count += temp_count
        return count
