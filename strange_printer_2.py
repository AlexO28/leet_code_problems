# There is a strange printer with the following two special requirements:
# On each turn, the printer will print a solid rectangular pattern of a single color on the grid. This will cover up the existing colors in the rectangle.
# Once the printer has used a color for the above operation, the same color cannot be used again.
# You are given a m x n matrix targetGrid, where targetGrid[row][col] is the color in the position (row, col) of the grid.
# Return true if it is possible to print the matrix targetGrid, otherwise, return false.
from collections import defaultdict
from typing import List


class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        colors = set()
        for i in range(len(targetGrid)):
            for j in range(len(targetGrid[0])):
                colors.add(targetGrid[i][j])
        color_bounds = {}
        for color in colors:
            min_row = len(targetGrid)
            max_row = -1
            min_col = len(targetGrid[0])
            max_col = -1
            for i in range(len(targetGrid)):
                for j in range(len(targetGrid[0])):
                    if targetGrid[i][j] == color:
                        min_row = min(min_row, i)
                        max_row = max(max_row, i)
                        min_col = min(min_col, j)
                        max_col = max(max_col, j)
            color_bounds[color] = [min_row, max_row, min_col, max_col]
        graph = defaultdict(set)
        in_degree = defaultdict(int)
        for color in colors:
            min_row, max_row, min_col, max_col = color_bounds[color]
            for i in range(min_row, max_row + 1):
                for j in range(min_col, max_col + 1):
                    if targetGrid[i][j] != color:
                        if targetGrid[i][j] not in graph[color]:
                            graph[color].add(targetGrid[i][j])
                            in_degree[targetGrid[i][j]] += 1
        queue = deque([color for color in colors if in_degree[color] == 0])
        printed_count = 0
        while queue:
            current_color = queue.popleft()
            printed_count += 1
            for next_color in graph[current_color]:
                in_degree[next_color] -= 1
                if in_degree[next_color] == 0:
                    queue.append(next_color)
        return printed_count == len(colors)
