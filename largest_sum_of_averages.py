# You are given an integer array nums and an integer k. You can partition the array into at most k non-empty adjacent subarrays. The score of a partition is the sum of the averages of each subarray.
# Note that the partition must use every integer in nums, and that the score is not necessarily an integer.
# Return the maximum score you can achieve of all the possible partitions. Answers within 10-6 of the actual answer will be accepted.
from functools import cache


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        return self.recursiveSumOfAverages(" ".join([str(num) for num in nums]), k)

    @cache
    def recursiveSumOfAverages(self, nums, k):
        nums = [int(num) for num in nums.split(" ")]
        if k == 1:
            return sum(nums)/len(nums)
        summa = 0
        max_val = None
        for j in range(len(nums)-k+1):
            summa += nums[j]
            cur_val = (summa/(j+1)) + self.recursiveSumOfAverages(" ".join([str(num) for num in nums[(j+1):]]), k-1)
            if max_val is None:
                max_val = cur_val
            else:
                max_val = max(max_val, cur_val)
        return max_val
