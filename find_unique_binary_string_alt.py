# Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.
from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums_10 = {int(num, 2): 1 for num in nums}
        i = 0
        while True:
            if i not in nums_10:
                line = "{0:b}".format(i)
                if len(line) < len(nums):
                    return "0"*(len(nums)-len(line)) + line
                else:
                    return line
            else:
                i += 1
