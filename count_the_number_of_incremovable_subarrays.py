# You are given a 0-indexed array of positive integers nums.
# A subarray of nums is called incremovable if nums becomes strictly increasing on removing the subarray. For example, the subarray [3, 4] is an incremovable subarray of [5, 3, 4, 6, 7] because removing this subarray changes the array [5, 3, 4, 6, 7] to [5, 6, 7] which is strictly increasing.
# Return the total number of incremovable subarrays of nums.
# Note that an empty array is considered strictly increasing.
# A subarray is a contiguous non-empty sequence of elements within an array.
from typing import List


class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                nums_copy = nums[:i] + nums[(j + 1):]
                if len(nums_copy) == 1:
                    res += 1
                else:
                    for k in range(1, len(nums_copy)):
                        if nums_copy[k] <= nums_copy[k - 1]:
                            break
                    else:
                        res += 1
        return res
