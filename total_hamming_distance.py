# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
# Given an integer array nums, return the sum of Hamming distances between all the pairs of the integers in nums.
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        total_distance = 0
        for i in range(31):
            count_one = 0
            count_zero = 0
            for num in nums:
                bit = (num >> i) & 1
                if bit:
                    count_one += 1
                else:
                    count_zero += 1
            total_distance += count_one * count_zero      
        return total_distance
