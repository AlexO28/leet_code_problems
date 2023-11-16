# Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        new_nums = [int(num, 2) for num in nums]
        for j in range(2 ** len(nums)):
            if j not in new_nums:
                new_str = "{0:b}".format(j)
                if len(new_str) == len(nums):
                    return new_str
                else:
                    return "0"*(len(nums)-len(new_str)) + new_str
