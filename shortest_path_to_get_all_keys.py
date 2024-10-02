# You are given an m x n grid grid where:
# '.' is an empty cell.
# '#' is a wall.
# '@' is the starting point.
# Lowercase letters represent keys.
# Uppercase letters represent locks.
# You start at the starting point and one move consists of walking one space in one of the four cardinal directions. You cannot walk outside the grid, or walk into a wall.
# If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.
# For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.
# Return the lowest number of moves to acquire all keys. If it is impossible, return -1.
from collections import deque


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        total_keys = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "@":
                    start_i = i
                    start_j = j
                elif grid[i][j].islower():
                    total_keys += 1
        directions = (-1, 0, 1, 0, -1)
        queue = deque([(start_i, start_j, 0)])
        visited = {(start_i, start_j, 0)}
        steps = 0
        while queue:
            for q in range(len(queue)):
                i, j, state = queue.popleft()
                if state == (1 << total_keys) - 1:
                    return steps
                for ind in range(4):
                    x = i + directions[ind]
                    y = j + directions[ind + 1]
                    next_state = state
                    if (x >= 0) and (x < len(grid)) and (y >= 0) and (y < len(grid[0])):
                        if not (
                            (grid[x][y] == "#")
                            or (
                                (grid[x][y].isupper())
                                and (state & (1 << (ord(grid[x][y]) - ord("A"))) == 0)
                            )
                        ):
                            if grid[x][y].islower():
                                next_state |= 1 << (ord(grid[x][y]) - ord("a"))
                            if (x, y, next_state) not in visited:
                                visited.add((x, y, next_state))
                                queue.append((x, y, next_state))
            steps += 1
        return -1
