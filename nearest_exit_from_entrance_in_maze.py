# You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.
# In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.
# Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.
from typing import List
from collections import deque


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        i, j = entrance
        q = deque([(i, j)])
        maze[i][j] = "+"
        res = 0
        while q:
            res += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                if i > 0:
                    next_i = i - 1
                    next_j = j
                    if maze[next_i][next_j] == ".":
                        if (
                            (next_i == 0)
                            or (next_j == 0)
                            or (next_i == len(maze) - 1)
                            or (next_j == len(maze[0]) - 1)
                        ):
                            return res
                        q.append((next_i, next_j))
                        maze[next_i][next_j] = "+"
                if i < len(maze) - 1:
                    next_i = i + 1
                    next_j = j
                    if maze[next_i][next_j] == ".":
                        if (
                            (next_i == 0)
                            or (next_j == 0)
                            or (next_i == len(maze) - 1)
                            or (next_j == len(maze[0]) - 1)
                        ):
                            return res
                        q.append((next_i, next_j))
                        maze[next_i][next_j] = "+"
                if j > 0:
                    next_i = i
                    next_j = j - 1
                    if maze[next_i][next_j] == ".":
                        if (
                            (next_i == 0)
                            or (next_j == 0)
                            or (next_i == len(maze) - 1)
                            or (next_j == len(maze[0]) - 1)
                        ):
                            return res
                        q.append((next_i, next_j))
                        maze[next_i][next_j] = "+"
                if j < len(maze[0]) - 1:
                    next_i = i
                    next_j = j + 1
                    if maze[next_i][next_j] == ".":
                        if (
                            (next_i == 0)
                            or (next_j == 0)
                            or (next_i == len(maze) - 1)
                            or (next_j == len(maze[0]) - 1)
                        ):
                            return res
                        q.append((next_i, next_j))
                        maze[next_i][next_j] = "+"
        return -1
