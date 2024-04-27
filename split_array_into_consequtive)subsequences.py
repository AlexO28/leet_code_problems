# You are given an integer array nums that is sorted in non-decreasing order.
# Determine if it is possible to split nums into one or more subsequences such that both of the following conditions are true:
# Each subsequence is a consecutive increasing sequence (i.e. each integer is exactly one more than the previous integer).
# All subsequences have a length of 3 or more.
# Return true if you can split nums according to the above conditions, or false otherwise.
import heapq
from collections import defaultdict


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        sequence_lengths = defaultdict(list)
        for num in nums:
            if sequence_lengths[num - 1]:
                shortest_sequence = heapq.heappop(sequence_lengths[num - 1])
                heapq.heappush(sequence_lengths[num], shortest_sequence + 1)
            else:
                heapq.heappush(sequence_lengths[num], 1)
        for sequence in sequence_lengths.values():
            if len(sequence) > 0:
                if sequence[0] <= 2:
                    return False
        return True
