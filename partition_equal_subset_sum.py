# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum, remainder = divmod(sum(nums), 2)      
        if remainder > 0:
            return False
        if max(nums) > total_sum:
            return False
        can_partition = [True] + [False] * total_sum      
        for num in nums:
            for j in range(total_sum, num - 1, -1):
                if (not can_partition[j]) and (can_partition[j - num]):
                    can_partition[j] = True
        return can_partition[total_sum]
