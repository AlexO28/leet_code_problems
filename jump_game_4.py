# Given an array of integers arr, you are initially positioned at the first index of the array.
# In one step you can jump from index i to index:
# i + 1 where: i + 1 < arr.length.
# i - 1 where: i - 1 >= 0.
# j where: arr[i] == arr[j] and i != j.
# Return the minimum number of steps to reach the last index of the array.
# Notice that you can not jump outside of the array at any time.
from typing import List
from collections import defaultdict, deque


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        index_map = defaultdict(list)
        for index, value in enumerate(arr):
            index_map[value].append(index)
        queue = deque([(0, 0)])
        visited = set([0])
        while queue:
            position, step_count = queue.popleft()
            if position == len(arr) - 1:
                return step_count
            else:
                step_count += 1
                for next_position in index_map[arr[position]]:
                    if next_position not in visited:
                        visited.add(next_position)
                        queue.append((next_position, step_count))
                del index_map[arr[position]]
                if (position + 1 < len(arr)) and ((position + 1) not in visited):
                    visited.add(position + 1)
                    queue.append((position + 1, step_count))
                if (position - 1 >= 0) and ((position - 1) not in visited):
                    visited.add(position - 1)
                    queue.append((position - 1, step_count))
        return -1
