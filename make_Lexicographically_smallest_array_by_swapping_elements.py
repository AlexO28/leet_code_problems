# You are given a 0-indexed array of positive integers nums and a positive integer limit.
# In one operation, you can choose any two indices i and j and swap nums[i] and nums[j] if |nums[i] - nums[j]| <= limit.
# Return the lexicographically smallest array that can be obtained by performing the operation any number of times.
# An array a is lexicographically smaller than an array b if in the first position where a and b differ, array a has an element that is less than the corresponding element in b. For example, the array [2,10,3] is lexicographically smaller than the array [10,2,3] because they differ at index 0 and 2 < 10.
from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        arr = sorted(zip(nums, range(len(nums))))
        ans = [0] * len(nums)
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums) and arr[j][0] - arr[j - 1][0] <= limit:
                j += 1
            idx = sorted(k for _, k in arr[i:j])
            for k, (x, _) in zip(idx, arr[i:j]):
                ans[k] = x
            i = j
        return ans
