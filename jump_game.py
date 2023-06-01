# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump_len = 0
        if len(nums) == 1:
            return True
        for num in nums[:(len(nums)-1)]:
            jump_len = max(num, jump_len - 1)
            if jump_len == 0:
                return False
        return True
