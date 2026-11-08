# You are given an array nums consisting of positive integers.
# You have to take each integer in the array, reverse its digits, and add it to the end of the array. You should apply this operation to the original integers in nums.
# Return the number of distinct integers in the final array.
class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        nums = set(nums)
        nums_alt = set()
        for num in nums:
            nums_alt.add(int(str(num)[::-1]))
        return len(nums | nums_alt)
