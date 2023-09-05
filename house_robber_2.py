# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    def rob_prev(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        else:
            n = len(nums)
            first_cand = nums[1]
            second_cand = nums[0]
            for i in range(0, n-2):
                temp_val = second_cand + nums[i+2]
                second_cand = max(first_cand, second_cand)
                first_cand = temp_val
            return round(max(first_cand, second_cand))

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_prev(nums[1:]), self.rob_prev(nums[:(len(nums) - 1)]))
