# Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].


import bisect


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = []
        temp = []
        for num in reversed(nums):
            id = bisect.bisect_left(temp, num)
            res.append(id)
            bisect.insort(temp, num)
        return res[::-1]
