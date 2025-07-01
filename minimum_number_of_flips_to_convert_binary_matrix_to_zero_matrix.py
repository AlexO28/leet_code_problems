# Given a m x n binary matrix mat. In one step, you can choose one cell and flip it and all the four neighbors of it if they exist (Flip is changing 1 to 0 and 0 to 1). A pair of cells are called neighbors if they share one edge.
# Return the minimum number of steps required to convert mat to a zero matrix or -1 if you cannot.
# A binary matrix is a matrix with all cells equal to 0 or 1 only.
# A zero matrix is a matrix with all cells equal to 0.
from typing import List
from collections import deque


class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        initial_state = sum(
            1 << (i * len(mat[0]) + j)
            for i in range(len(mat))
            for j in range(len(mat[0]))
            if mat[i][j]
        )
        queue = deque([initial_state])
        visited = {initial_state}
        flips = 0
        directions = [0, -1, 0, 1, 0, 0]
        while queue:
            for _ in range(len(queue)):
                current_state = queue.popleft()
                if current_state == 0:
                    return flips
                for i in range(len(mat)):
                    for j in range(len(mat[0])):
                        next_state = current_state
                        for k in range(5):
                            x = i + directions[k]
                            y = j + directions[k + 1]
                            if (0 <= x < len(mat)) and (0 <= y < len(mat[0])):
                                next_state ^= 1 << (x * len(mat[0]) + y)
                        if next_state not in visited:
                            visited.add(next_state)
                            queue.append(next_state)
            flips += 1
        return -1
