# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        struct = deque()
        for i in range(k):
            while struct and (nums[i] >= nums[struct[-1]]):
                struct.pop()
            struct.append(i)
        for i in range(k, len(nums)):
            res.append(nums[struct[0]])
            while struct and (struct[0] <= i-k):
                struct.popleft()
            while struct and (nums[i] >= nums[struct[-1]]):
                struct.pop()
            struct.append(i)
        res.append(nums[struct[0]])
        return res
