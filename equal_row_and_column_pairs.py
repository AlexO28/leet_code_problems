# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        row_hashes = {}
        for i in range(len(grid)):
            line = "-".join([str(elem) for elem in grid[i]])
            if line in row_hashes:
                row_hashes[line] += 1
            else:
                row_hashes[line] = 1
        res = 0
        for j in range(len(grid[0])):
            temp = []
            for i in range(len(grid)):
                temp.append(grid[i][j])
            line = "-".join([str(elem) for elem in temp])
            if line in row_hashes:
                res += row_hashes[line]
        return res
