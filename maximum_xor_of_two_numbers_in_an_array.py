# Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 <= i <= j < n.
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        maximum_xor = 0
        mask = 0
        for i in range(31, -1, -1):
            mask = mask | (1 << i)
            prefixes = set()
            for num in nums:
                prefixes.add(num & mask)
            proposed_max = maximum_xor | (1 << i)
            for prefix in prefixes:
                if (prefix ^ proposed_max) in prefixes:
                    maximum_xor = proposed_max
                    break                  
        return maximum_xor
