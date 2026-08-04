# You are given a 0-indexed array nums of n integers, and an integer k.
# The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.
# Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.
# The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part.
from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        win_len = 2 * k + 1
        if len(nums) < win_len:
            return [-1] * len(nums)
        summa = sum(nums[:win_len])
        res = [summa]
        if len(nums) > win_len:
            for i in range(1, len(nums) - win_len + 1):
                res.append(res[-1] - nums[i - 1] + nums[i + win_len - 1])
        res = [elem // win_len for elem in res]
        if k > 0:
            for i in range(k):
                res.insert(0, -1)
                res.append(-1)
        return res
