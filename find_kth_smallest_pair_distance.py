# The distance of a pair of integers a and b is defined as the absolute difference between a and b.
# Given an integer array nums and an integer k, return the kth smallest distance among all the pairs nums[i] and nums[j] where 0 <= i < j < nums.length.
from bisect import bisect_left


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        self.nums = nums
        return bisect_left(range(nums[-1] - nums[0] + 1), k, key=self.countPairsWithMaxDistance)

    def countPairsWithMaxDistance(self, dist):
        count = 0
        for i in range(len(self.nums)):
            count += i - bisect_left(self.nums, self.nums[i] - dist, 0, i)
        return count
