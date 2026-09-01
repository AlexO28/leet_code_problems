# You are given an m x n grid classroom where a student volunteer is tasked with cleaning up litter scattered around the room. Each cell in the grid is one of the following:
# 'S': Starting position of the student
# 'L': Litter that must be collected (once collected, the cell becomes empty)
# 'R': Reset area that restores the student's energy to full capacity, regardless of their current energy level (can be used multiple times)
# 'X': Obstacle the student cannot pass through
# '.': Empty space
# You are also given an integer energy, representing the student's maximum energy capacity. The student starts with this energy from the starting position 'S'.
# Each move to an adjacent cell (up, down, left, or right) costs 1 unit of energy. If the energy reaches 0, the student can only continue if they are on a reset area 'R', which resets the energy to its maximum capacity energy.
# Return the minimum number of moves required to collect all litter items, or -1 if it's impossible.
from typing import List


class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        d = [[0] * len(classroom[0]) for _ in range(len(classroom))]
        x = 0
        y = 0
        cnt = 0
        for i, row in enumerate(classroom):
            for j, c in enumerate(row):
                if c == "S":
                    x = i
                    y = j
                elif c == "L":
                    d[i][j] = cnt
                    cnt += 1
        if cnt == 0:
            return 0
        vis = [
            [
                [[False] * (1 << cnt) for _ in range(energy + 1)]
                for _ in range(len(classroom[0]))
            ]
            for _ in range(len(classroom))
        ]
        q = [(x, y, energy, (1 << cnt) - 1)]
        vis[x][y][energy][(1 << cnt) - 1] = True
        dirs = (-1, 0, 1, 0, -1)
        ans = 0
        while q:
            t = q
            q = []
            for i, j, cur_energy, mask in t:
                if mask == 0:
                    return ans
                if cur_energy <= 0:
                    continue
                for k in range(4):
                    x = i + dirs[k]
                    y = j + dirs[k + 1]
                    if (
                        0 <= x < len(classroom)
                        and 0 <= y < len(classroom[0])
                        and classroom[x][y] != "X"
                    ):
                        nxt_energy = (
                            energy if classroom[x][y] == "R" else cur_energy - 1
                        )
                        nxt_mask = mask
                        if classroom[x][y] == "L":
                            nxt_mask &= ~(1 << d[x][y])
                        if not vis[x][y][nxt_energy][nxt_mask]:
                            vis[x][y][nxt_energy][nxt_mask] = True
                            q.append((x, y, nxt_energy, nxt_mask))
            ans += 1
        return -1
