# The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.
# For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
# Given an array nums, return the sum of all XOR totals for every subset of nums. 
# Note: Subsets with the same elements should be counted multiple times.
# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.'
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        return sum(self.calculateXOR(nums))
        
    def calculateXOR(self, arr):
        if len(arr) == 1:
            return [arr[0]]
        right_res = self.calculateXOR(arr[1:])
        res = [arr[0]]
        for elem in right_res:
            res.append(elem)
            res.append(arr[0] ^ elem)
        return res
