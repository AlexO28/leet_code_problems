# Given an integer array nums, return the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.
from bisect import bisect_left


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums = [num for num in nums if num > 0]
        if len(nums) < 3:
            return 0
        nums.sort()
        count = 0
        for i in range(len(nums)-2):
            for j in range(i + 1, len(nums) - 1):
                k = bisect_left(nums, nums[i] + nums[j], lo=j + 1) - 1
                count += k - j
        return count
