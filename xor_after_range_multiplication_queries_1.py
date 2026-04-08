# You are given an integer array nums of length n and a 2D integer array queries of size q, where queries[i] = [li, ri, ki, vi].
# For each query, you must apply the following operations in order:
# Set idx = li.
# While idx <= ri:
# Update: nums[idx] = (nums[idx] * vi) % (109 + 7)
# Set idx += ki.
# Return the bitwise XOR of all elements in nums after processing all queries.
from typing import List


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 1000000007
        for query in queries:
            idx = query[0]
            while idx <= query[1]:
                nums[idx] = (nums[idx] * query[3]) % (MOD)
                idx += query[2]
        res = 0
        for num in nums:
            res ^= num
        return res
