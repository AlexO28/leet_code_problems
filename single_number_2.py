# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        num_prev = nums[0] - 1
        count = -1
        for num in nums:
            if num == num_prev:
                count = 1
            else:
                if count == 0:
                    return num_prev
                count = 0
            num_prev = num
        return num
