# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        cur_prod = 1
        count = 0
        start = 0
        for cur in range(len(nums)):
            cur_prod *= nums[cur]
            while (start < cur) and (cur_prod >= k):
                cur_prod /= nums[start]
                start += 1
            if cur_prod < k:
                count += cur - start + 1
        return count
