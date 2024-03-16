# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        cur_sum = 0
        for i in range(int(len(nums)/2)):
            cur_sum += min(nums[2*i], nums[2*i+1])
        return cur_sum
