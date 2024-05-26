# You are given an integer array nums where the largest integer is unique.
# Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        nums_save = nums.copy()
        nums_save.sort(reverse=True)
        if nums_save[0] >= 2*nums_save[1]:
            return nums.index(nums_save[0])
        else:
            return -1
