# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).
# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def bfs(queue, visited):
            while queue:
                for j in range(len(queue)):
                    row, col = queue.popleft()
                    for delta_row, delta_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                        new_row, new_col = row + delta_row, col + delta_col
                        if (0 <= new_row < num_rows) and\
                           (0 <= new_col < num_columns) and\
                           ((new_row, new_col) not in visited) and\
                           (heights[new_row][new_col] >= heights[row][col]):
                            visited.add((new_row, new_col))
                            queue.append((new_row, new_col))

        num_rows = len(heights)
        num_columns = len(heights[0])      
        visited_pacific = set()
        visited_atlantic = set()
        pacific_queue = deque()
        atlantic_queue = deque()
        for row in range(num_rows):
            for col in range(num_columns):
                if (row == 0) or (col == 0):
                    visited_pacific.add((row, col))
                    pacific_queue.append((row, col))
                if (row == num_rows - 1) or (col == num_columns - 1):
                    visited_atlantic.add((row, col))
                    atlantic_queue.append((row, col))
        bfs(pacific_queue, visited_pacific)
        bfs(atlantic_queue, visited_atlantic)
        return [(row, col) for row in range(num_rows) for col in range(num_columns) 
                if (row, col) in visited_pacific and (row, col) in visited_atlantic]
