# You are given an integer array nums.
# A subarray is called balanced if the number of distinct even numbers in the subarray is equal to the number of distinct odd numbers.
# Return the length of the longest balanced subarray.
from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        ans = 0
        for i in range(len(nums)):
            cnt = [0, 0]
            vis = set()
            for j in range(i, len(nums)):
                if nums[j] not in vis:
                    cnt[nums[j] % 2] += 1
                    vis.add(nums[j])
                if cnt[0] == cnt[1]:
                    ans = max(ans, j - i + 1)
        return ans
