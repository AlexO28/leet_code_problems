# Given an array of integers arr and an integer d. In one step you can jump from index i to index:
# i + x where: i + x < arr.length and  0 < x <= d.
# i - x where: i - x >= 0 and  0 < x <= d.
# In addition, you can only jump from index i to index j if arr[i] > arr[j] and arr[i] > arr[k] for all indices k between i and j (More formally min(i, j) < k < max(i, j)).
# You can choose any index of the array and start jumping. Return the maximum number of indices you can visit.
# Notice that you can not jump outside of the array at any time.
from typing import List


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        jumps = [1] * len(arr)
        for height, position in sorted(zip(arr, range(len(arr)))):
            for left in range(position - 1, -1, -1):
                if (position - left > d) or (arr[left] >= height):
                    break
                else:
                    jumps[position] = max(jumps[position], 1 + jumps[left])
            for right in range(position + 1, len(arr)):
                if (right - position > d) or (arr[right] >= height):
                    break
                else:
                    jumps[position] = max(jumps[position], 1 + jumps[right])
        return max(jumps)
