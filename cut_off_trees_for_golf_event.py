# You are asked to cut off all the trees in a forest for a golf event. The forest is represented as an m x n matrix. In this matrix:
# 0 means the cell cannot be walked through.
# 1 represents an empty cell that can be walked through.
# A number greater than 1 represents a tree in a cell that can be walked through, and this number is the tree's height.
# In one step, you can walk in any of the four directions: north, east, south, and west. If you are standing in a cell with a tree, you can choose whether to cut it off.
# You must cut off the trees in order from shortest to tallest. When you cut off a tree, the value at its cell becomes 1 (an empty cell).
# Starting from the point (0, 0), return the minimum steps you need to walk to cut off all the trees. If you cannot cut off all the trees, return -1.
from heapq import heappop, heappush


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        self.row = len(forest)
        self.column = len(forest[0])
        self.forest = forest
        trees = [(forest[i][j], i, j) for i in range(self.row) for j in range(self.column) if forest[i][j] > 1]
        trees.sort()
        current_i = 0
        current_j = 0
        total_steps = 0
        for k, target_i, target_j in trees:
            steps_to_next_tree = self.bfs(current_i, current_j, target_i, target_j)
            if steps_to_next_tree == -1:
                return -1
            total_steps += steps_to_next_tree
            current_i = target_i
            current_j = target_j
        return total_steps

    def bfs(self, start_i, start_j, dest_i, dest_j):
        queue = [(self.manhattan_distance(start_i, start_j, dest_i, dest_j), start_i, start_j)]
        distance = {start_i * self.column + start_j: 0}
        while queue:
            temp, curr_i, curr_j = heappop(queue)
            current_step = distance[curr_i * self.column + curr_j]
            if (curr_i, curr_j) == (dest_i, dest_j):
                return current_step
            for delta_i, delta_j in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                next_i = curr_i + delta_i
                next_j = curr_j + delta_j
                if 0 <= next_i < self.row and 0 <= next_j < self.column and self.forest[next_i][next_j] > 0:
                    next_position_key = next_i * self.column + next_j
                    if next_position_key not in distance or distance[next_position_key] > current_step + 1:
                        distance[next_position_key] = current_step + 1
                        heappush(queue, (distance[next_position_key] + self.manhattan_distance(next_i, next_j, dest_i, dest_j), next_i, next_j))
        return -1

    def manhattan_distance(self, i, j, x, y):
        return abs(i - x) + abs(j - y)
