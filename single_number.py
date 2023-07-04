# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

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
