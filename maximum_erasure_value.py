# You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.
# Return the maximum score you can get by erasing exactly one subarray.
# An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = 0
        max_sum = -1
        arr = [nums[0]]
        cur_sum = nums[0]
        while left < len(nums):
            max_sum = max(max_sum, cur_sum)
            right += 1
            if right == len(nums):
                break
            found = False
            while nums[right] in arr:
                found = True
                cur_sum -= arr[0]
                del arr[0]
                left += 1
            arr.append(nums[right])
            cur_sum += nums[right]
        return max_sum
