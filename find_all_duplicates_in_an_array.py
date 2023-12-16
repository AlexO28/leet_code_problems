# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return []
        nums.sort()
        res = []
        num_prev = nums[0]
        for j in range(1, len(nums)):
            if nums[j] == num_prev:
                res.append(num_prev)
            else:
                num_prev = nums[j]
        return res
