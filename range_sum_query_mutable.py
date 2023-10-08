# Given an integer array nums, handle multiple queries of the following types:
# Update the value of an element in nums.
# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.summa = sum(nums)

    def update(self, index: int, val: int) -> None:
        self.summa = self.summa - self.nums[index] + val
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        if (left == 0) & (right == len(self.nums) - 1):
            return self.summa
        elif left == 0:
            return self.summa - sum(self.nums[right+1:])
        elif right == len(self.nums) - 1:
            return self.summa - sum(self.nums[:left])
        else:
            return self.summa - sum(self.nums[:left]) - sum(self.nums[right+1:])

