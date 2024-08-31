# You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
# Return the size of the largest island in grid after applying this operation.
# An island is a 4-directionally connected group of 1s.
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        if len(grid) == 1:
            return 1
        n = len(grid)
        self.parents = list(range(n * n))
        self.set_sizes = [1] * (n * n)
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] > 0:
                    for a, b in [[0, -1], [-1, 0]]:
                        x = i + a
                        y = j + b
                        if (x >= 0) and (x < n) and (y >= 0) and (y < n):
                            if grid[x][y] > 0:
                                self.union_sets(x * n + y, i * n + j)
        max_island_size = max(self.set_sizes)
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 0:
                    visited_roots = set()
                    temp_size = 1
                    for a, b in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                        x = i + a
                        y = j + b
                        if (x >= 0) and (x < n) and (y >= 0) and (y < n):
                            if grid[x][y] > 0:
                                root = self.find_root(x * n + y)
                                if root not in visited_roots:
                                    visited_roots.add(root)
                                    temp_size += self.set_sizes[root]
                    max_island_size = max(max_island_size, temp_size)     
        return max_island_size

    def union_sets(self, set1, set2):
        root1 = self.find_root(set1)
        root2 = self.find_root(set2)
        if root1 != root2:
            self.parents[root1] = root2
            self.set_sizes[root2] += self.set_sizes[root1]

    def find_root(self, element):
        if self.parents[element] != element:
            self.parents[element] = self.find_root(self.parents[element])
        return self.parents[element]
