# Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.
# In one move, you can increment n - 1 elements of the array by 1.
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_val = min(nums)
        return sum([num-min_val for num in nums])
