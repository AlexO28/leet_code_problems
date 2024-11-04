# Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
# Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
# Return any answer array that satisfies this condition.
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        evens = []
        odds = []
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                evens.append(nums[i])
            else:
                odds.append(nums[i])
        res = []
        for i in range(len(evens)):
            res.append(evens[i])
            res.append(odds[i])
        return res
