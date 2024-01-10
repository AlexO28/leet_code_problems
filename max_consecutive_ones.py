# Given a binary array nums, return the maximum number of consecutive 1's in the array.
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for j in range(len(nums)):
            if nums[j] == 1:
                count += 1
            else:
                res = max(res, count)
                count = 0
        return max(res, count)
