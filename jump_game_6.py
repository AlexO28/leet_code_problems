# You are given a 0-indexed integer array nums and an integer k.
# You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.
# You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.
# Return the maximum score you can get.
from typing import List
from collections import deque


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        f = [0] * len(nums)
        q = deque([0])
        for i in range(len(nums)):
            if i - q[0] > k:
                q.popleft()
            f[i] = nums[i] + f[q[0]]
            while q and f[q[-1]] <= f[i]:
                q.pop()
            q.append(i)
        return f[-1]
