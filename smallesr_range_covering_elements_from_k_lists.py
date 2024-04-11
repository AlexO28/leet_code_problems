# You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.
import heapq
import math


class Node:
    def __init__(self, data, row, next_col):
        self.data = data
        self.row = row
        self.next_col = next_col
 
    def __lt__(self, other):
        return self.data < other.data


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        if len(nums) == 1:
            return [nums[0][0], nums[0][0]]
        min_heap = []
        max_value = -math.inf
        smallest_range = math.inf
        start = -1
        end = -1
        for i in range(len(nums)):
            heapq.heappush(min_heap, Node(nums[i][0], i, 0))
            max_value = max(max_value, nums[i][0]) 
        while min_heap:
            node = heapq.heappop(min_heap)
            min_value = node.data
            if smallest_range > max_value - min_value:
                smallest_range = max_value - min_value
                start = min_value
                end = max_value
            row = node.row
            next_col = node.next_col
            if next_col + 1 < len(nums[row]):
                heapq.heappush(min_heap, Node(nums[row][next_col + 1], row, next_col + 1))
                max_value = max(max_value, nums[row][next_col + 1])
            else:
                break
        return [start, end]
