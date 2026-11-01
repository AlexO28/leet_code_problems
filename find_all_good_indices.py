# You are given a 0-indexed integer array nums of size n and a positive integer k.
# We call an index i in the range k <= i < n - k good if the following conditions are satisfied:
# The k elements that are just before the index i are in non-increasing order.
# The k elements that are just after the index i are in non-decreasing order.
# Return an array of all good indices sorted in increasing order.
class Solution:
    def goodIndices(self, nums: list[int], k: int) -> list[int]:
        before = [1]
        cur = 1
        for j in range(1, len(nums)):
            if nums[j] <= nums[j - 1]:
                cur += 1
                before.append(cur)
            else:
                cur = 1
                before.append(cur)
        after = [1]
        cur = 1
        for j in range(len(nums) - 2, -1, -1):
            if nums[j] <= nums[j + 1]:
                cur += 1
                after.append(cur)
            else:
                cur = 1
                after.append(cur)
        after = after[::-1]
        res = []
        for j in range(1, len(before) - 1):
            if (before[j - 1] >= k) and (after[j + 1] >= k):
                res.append(j)
        return res
