# The frequency of an element is the number of times it occurs in an array.
# You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.
# Return the maximum possible frequency of an element after performing at most k operations.

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        max_val = 0
        summa = 0
        nums.sort()
        i = 0
        for j in range(len(nums)):
            summa += nums[j]
            while k < nums[j] * (j - i + 1) - summa:
                summa -= nums[i]
                i += 1
            max_val = max(max_val, j - i + 1)
        return max_val
