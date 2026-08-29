# Given an integer array num sorted in non-decreasing order.
# You can perform the following operation any number of times:
# Choose two indices, i and j, where nums[i] < nums[j].
# Then, remove the elements at indices i and j from nums. The remaining elements retain their original order, and the array is re-indexed.
# Return the minimum length of nums after applying the operation zero or more times.
from typing import List


class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        self.nums = nums
        start_ind = 0
        end_ind = len(nums) // 2
        while end_ind - start_ind > 1:
            mid = (end_ind + start_ind) // 2
            if self.check(mid):
                start_ind = mid
            else:
                end_ind = mid
        if self.check(end_ind):
            ind = end_ind
        else:
            ind = start_ind
        return len(nums) - 2 * ind

    def check(self, k):
        for i in range(k):
            if self.nums[i] >= self.nums[len(self.nums) - k + i]:
                return False
        return True
