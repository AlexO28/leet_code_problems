# Given the root of a binary tree, calculate the vertical order traversal of the binary tree.
# For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).
# The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.
# Return the vertical order traversal of the binary tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.nodes = []
        self.search(root, 0, 0)
        self.nodes.sort(key = lambda x: (x[1], x[0], x[2]))
        result = []
        prev_vertical_distance = float("-inf")
        for level, vertical_distance, value in self.nodes:
            if prev_vertical_distance != vertical_distance:
                result.append([])
                prev_vertical_distance = vertical_distance
            result[-1].append(value)
        return result

    def search(self, node, level, vertical_distance):
        if node:
            self.nodes.append([level, vertical_distance, node.val])
            self.search(node.left, level + 1, vertical_distance - 1)
            self.search(node.right, level + 1, vertical_distance + 1)
