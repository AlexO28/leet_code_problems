# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
# A subarray is a contiguous part of the array.
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        if len(nums) == 1:
            if goal == nums[0]:
                return 1
            else:
                return 0
        left1 = 0
        left2 = 0
        sum1 = 0
        sum2 = 0
        i = 0
        number_of_hits = 0
        while i < len(nums):
            sum1 += nums[i]
            sum2 += nums[i]
            while (left1 <= i) and (sum1 > goal):
                sum1 -= nums[left1]
                left1 += 1
            while left2 <= i and sum2 >= goal:
                sum2 -= nums[left2]
                left2 += 1
            number_of_hits += left2 - left1
            i += 1
        return number_of_hits
