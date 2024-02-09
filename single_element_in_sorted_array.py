# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
# Return the single element that appears only once.
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i = 0
        while i+1 < len(nums):
            if nums[i] == nums[i+1]:
                i += 2
            else:
                return nums[i]
        return nums[-1]
