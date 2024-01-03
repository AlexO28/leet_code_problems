# Given a n * n matrix grid of 0's and 1's only. We want to represent grid with a Quad-Tree.
# Return the root of the Quad-Tree representing grid.
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.constructQuadTree(grid, 0, 0, len(grid)-1, len(grid[0])-1)

    def constructQuadTree(self, grid, start_x, start_y, end_x, end_y):
        print(start_x, start_y, end_x, end_y)
        if start_x == end_x:
            return Node(grid[start_x][start_y] == 1, True, None, None, None, None)
        else:
            max_val = -1
            min_val = 2
            for i in range(start_x, end_x+1):
                for j in range(start_y, end_y+1):
                    max_val = max(max_val, grid[i][j])
                    min_val = min(min_val, grid[i][j])
            if max_val == min_val:
                return Node(max_val == 1, True, None, None, None, None)
            mid_x = (end_x + start_x) // 2
            mid_y = (end_y + start_y) // 2
            top_left = self.constructQuadTree(grid, start_x, start_y, mid_x, mid_y)
            bottom_left = self.constructQuadTree(grid, mid_x+1, start_y, end_x, mid_y)
            top_right = self.constructQuadTree(grid, start_x, mid_y+1, mid_x, end_y)
            bottom_right = self.constructQuadTree(grid, mid_x+1, mid_y+1, end_x, end_y)
            return Node(True, False, top_left, top_right, bottom_left, bottom_right)
 
