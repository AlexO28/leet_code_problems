# You are given an m x n binary grid, where each 1 represents a brick and 0 represents an empty space. A brick is stable if:
# It is directly connected to the top of the grid, or
# At least one other brick in its four adjacent cells is stable.
# You are also given an array hits, which is a sequence of erasures we want to apply. Each time we want to erase the brick at the location hits[i] = (rowi, coli). The brick on that location (if it exists) will disappear. Some other bricks may no longer be stable because of that erasure and will fall. Once a brick falls, it is immediately erased from the grid (i.e., it does not land on other stable bricks).
# Return an array result, where each result[i] is the number of bricks that will fall after the ith erasure is applied.
# Note that an erasure may refer to a location with no brick, and if it does, no bricks drop.
class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        self.parent = list(range(len(grid)*len(grid[0]) + 1))
        self.size = [1]*(len(grid)*len(grid[0]) + 1)
        grid_copy = []
        for i in range(len(grid)):
            temp_arr = []
            for j in range(len(grid[0])):
                temp_arr.append(grid[i][j])
            grid_copy.append(temp_arr.copy())
        for hit in hits:
            grid_copy[hit[0]][hit[1]] = 0
        for j in range(len(grid[0])):
            if grid_copy[0][j] == 1:
                self.union(j, len(grid)*len(grid[0]))
        for i in range(1, len(grid)):
            for j in range(len(grid[0])):
                if grid_copy[i][j] > 0:
                    if grid_copy[i-1][j] > 0:
                        self.union(i*len(grid[0]) + j, (i-1)*len(grid[0]) + j)
                    if (j > 0) and (grid_copy[i][j-1] > 0):
                        self.union(i*len(grid[0]) + j, i*len(grid[0]) + j - 1)
        res = []
        for k in range(len(hits)-1, -1, -1):
            if grid[hits[k][0]][hits[k][1]] == 0:
                res.append(0)
            else:
                grid_copy[hits[k][0]][hits[k][1]] = 1
                prev_size = self.size[self.find(len(grid) * len(grid[0]))]
                if hits[k][0] == 0:
                    self.union(hits[k][1], len(grid) * len(grid[0]))
                for delta_row, delta_col in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    x = hits[k][0] + delta_row
                    y = hits[k][1] + delta_col
                    if (x >= 0) and (x < len(grid)) and (y >= 0) and (y < len(grid[0])):
                        if grid_copy[x][y] > 0:
                            self.union(hits[k][0] * len(grid[0]) + hits[k][1], x * len(grid[0]) + y)
                curr_size = self.size[self.find(len(grid[0]) * len(grid))]
                res.append(max(0, curr_size - prev_size - 1))
        return res[::-1]

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.size[root_b] += self.size[root_a]
            self.parent[root_a] = root_b

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
