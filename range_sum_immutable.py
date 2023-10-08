# Given an integer array nums, handle multiple queries of the following type:
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left:(right+1)])
