# Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:
# answer[i] % answer[j] == 0, or
# answer[j] % answer[i] == 0
# If there are multiple solutions, return any of them.
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        nums.sort()
        dp = [[]]
        for j in range(len(nums)):
            dp.append([])
        for j in range(len(nums)-1, -1, -1):
            if j == len(nums) - 1:
                dp[len(nums)-1] = [nums[len(nums) - 1]]
            else:
                res_list = []
                for k in range(j+1, len(nums)):
                    if nums[k] % nums[j] == 0:
                        temp_list = dp[k]
                        if len(temp_list) > len(res_list):
                            res_list = temp_list
                dp[j] = [nums[j]]
                dp[j].extend(res_list)
        res_list = []
        for j in range(len(nums)):
            if len(dp[j]) > len(res_list):
                res_list = dp[j]
        return res_list
