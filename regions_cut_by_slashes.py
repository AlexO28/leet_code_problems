# An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.
# Given the grid grid represented as a string array, return the number of regions.
# Note that backslash characters are escaped, so a '\' is represented as '\\'.
from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        self.region_count = 4 * (len(grid) ** 2)
        self.parent = list(range(self.region_count))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cell_index = i*len(grid) + j
                if i < len(grid) - 1:
                    self.union_sets(4 * cell_index + 2, 4 * (cell_index + len(grid)))
                if j < len(grid) - 1:
                    self.union_sets(4 * cell_index + 1, 4 * (cell_index + 1) + 3)
                if grid[i][j] == "/":
                    self.union_sets(4 * cell_index, 4 * cell_index + 3)
                    self.union_sets(4 * cell_index + 1, 4 * cell_index + 2)
                elif grid[i][j] == "\\":
                    self.union_sets(4 * cell_index, 4 * cell_index + 1)
                    self.union_sets(4 * cell_index + 2, 4 * cell_index + 3)
                else:
                    self.union_sets(4 * cell_index, 4 * cell_index + 1)
                    self.union_sets(4 * cell_index + 1, 4 * cell_index + 2)
                    self.union_sets(4 * cell_index + 2, 4 * cell_index + 3)
        return self.region_count


    def find_set(self, root_index):
        if self.parent[root_index] != root_index:
            self.parent[root_index] = self.find_set(self.parent[root_index])
        return self.parent[root_index]


    def union_sets(self, set_a, set_b):
        root_a = self.find_set(set_a)
        root_b = self.find_set(set_b)
        if root_a != root_b:
            self.parent[root_a] = root_b
            self.region_count -= 1
