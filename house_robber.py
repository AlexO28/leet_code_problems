# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

class Solution:
    def rob(self, nums: List[int]) -> int:
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
