# Given an array of non-negative integers arr, you are initially positioned at start index of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.
# Notice that you can not jump outside of the array at any time.
from typing import List
from collections import deque


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        max_val = len(arr) + 1
        distances = [max_val] * len(arr)
        distances[start] = 0
        q = deque()
        q.append(start)
        while q:
            ind = q.pop()
            if ind >= arr[ind]:
                left = ind - arr[ind]
            else:
                left = -1
            if ind + arr[ind] < len(arr):
                right = ind + arr[ind]
            else:
                right = -1
            next_val = distances[ind] + 1
            if (left >= 0) and (distances[left] > next_val):
                distances[left] = next_val
                q.append(left)
            next_val = distances[ind] + 1
            if (right >= 0) and (distances[right] > next_val):
                distances[right] = next_val
                q.append(right)
        for i in range(len(arr)):
            if (arr[i] == 0) and (distances[i] != max_val):
                return True
        return False
