# A game is played by a cat and a mouse named Cat and Mouse.
# The environment is represented by a grid of size rows x cols, where each element is a wall, floor, player (Cat, Mouse), or food.
# Players are represented by the characters 'C'(Cat),'M'(Mouse).
# Floors are represented by the character '.' and can be walked on.
# Walls are represented by the character '#' and cannot be walked on.
# Food is represented by the character 'F' and can be walked on.
# There is only one of each character 'C', 'M', and 'F' in grid.
# Mouse and Cat play according to the following rules:
# Mouse moves first, then they take turns to move.
# During each turn, Cat and Mouse can jump in one of the four directions (left, right, up, down). They cannot jump over the wall nor outside of the grid.
# catJump, mouseJump are the maximum lengths Cat and Mouse can jump at a time, respectively. Cat and Mouse can jump less than the maximum length.
# Staying in the same position is allowed.
# Mouse can jump over Cat.
# The game can end in 4 ways:
# If Cat occupies the same position as Mouse, Cat wins.
# If Cat reaches the food first, Cat wins.
# If Mouse reaches the food first, Mouse wins.
# If Mouse cannot get to the food within 1000 turns, Cat wins.
# Given a rows x cols matrix grid and two integers catJump and mouseJump, return true if Mouse can win the game if both Cat and Mouse play optimally, otherwise return false.
from typing import List
from itertools import pairwise
from collections import deque


class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        cat_start = 0
        mouse_start = 0
        food = 0
        dirs = (-1, 0, 1, 0, -1)
        prod = len(grid) * len(grid[0])
        g_mouse = [[] for i in range(prod)]
        g_cat = [[] for i in range(prod)]
        for i, row in enumerate(grid):
            for j, c in enumerate(row):
                if c == "#":
                    continue
                v = i * len(grid[0]) + j
                if c == "C":
                    cat_start = v
                elif c == "M":
                    mouse_start = v
                elif c == "F":
                    food = v
                for a, b in pairwise(dirs):
                    for k in range(mouseJump + 1):
                        x = i + k * a
                        y = j + k * b
                        if not (
                            0 <= x < len(grid)
                            and 0 <= y < len(grid[0])
                            and grid[x][y] != "#"
                        ):
                            break
                        g_mouse[v].append(x * len(grid[0]) + y)
                    for k in range(catJump + 1):
                        x = i + k * a
                        y = j + k * b
                        if not (
                            0 <= x < len(grid)
                            and 0 <= y < len(grid[0])
                            and grid[x][y] != "#"
                        ):
                            break
                        g_cat[v].append(x * len(grid[0]) + y)
        return self.calc(g_mouse, g_cat, mouse_start, cat_start, food) == 1

    def calc(
        self,
        g_mouse,
        g_cat,
        mouse_start,
        cat_start,
        hole,
    ):
        self.g_cat = g_cat
        self.g_mouse = g_mouse
        degree = [
            [[0, 0] for i in range(len(self.g_mouse))] for j in range(len(self.g_mouse))
        ]
        for i in range(len(self.g_mouse)):
            for j in range(len(self.g_mouse)):
                degree[i][j][0] = len(self.g_mouse[i])
                degree[i][j][1] = len(self.g_cat[j])
        self.ans = [
            [[0, 0] for i in range(len(self.g_mouse))] for j in range(len(self.g_mouse))
        ]
        q = deque()
        for i in range(len(self.g_mouse)):
            self.ans[hole][i][1] = 1
            self.ans[i][hole][0] = 2
            self.ans[i][i][1] = 2
            self.ans[i][i][0] = 2
            q.append((hole, i, 1))
            q.append((i, hole, 0))
            q.append((i, i, 0))
            q.append((i, i, 1))
        while q:
            state = q.popleft()
            t = self.ans[state[0]][state[1]][state[2]]
            for prev_state in self.get_prev_states(state):
                pm, pc, pt = prev_state
                if pt == t - 1:
                    self.ans[pm][pc][pt] = t
                    q.append(prev_state)
                else:
                    degree[pm][pc][pt] -= 1
                    if degree[pm][pc][pt] == 0:
                        self.ans[pm][pc][pt] = t
                        q.append(prev_state)
        return self.ans[mouse_start][cat_start][0]

    def get_prev_states(self, state):
        m, c, t = state
        pt = t ^ 1
        pre = []
        if pt == 1:
            for pc in self.g_cat[c]:
                if self.ans[m][pc][1] == 0:
                    pre.append((m, pc, pt))
        else:
            for pm in self.g_mouse[m]:
                if self.ans[pm][c][0] == 0:
                    pre.append((pm, c, 0))
        return pre
