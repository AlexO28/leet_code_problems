# Given the root of a binary tree with unique values and the values of two different nodes of the tree x and y, return true if the nodes corresponding to the values x and y in the tree are cousins, or false otherwise.
# Two nodes of a binary tree are cousins if they have the same depth with different parents.
# Note that in a binary tree, the root node is at the depth 0, and children of each depth k node are at the depth k + 1.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if (root.val == x) or (root.val == y):
            return False
        level_left, parent_left = self.calculateDepth(root, x)
        level_right, parent_right = self.calculateDepth(root, y)
        if parent_left == parent_right:
            return False
        return level_left == level_right


    def calculateDepth(self, tree, val):
        if (tree.left is None) and (tree.right is None):
            return -1, None
        if tree.left is not None:
            if tree.left.val == val:
                return 1, tree.val
            candidate, parent = self.calculateDepth(tree.left, val)
            if candidate >= 0:
                return candidate + 1, parent
        if tree.right is not None:
            if tree.right.val == val:
                return 1, tree.val
            candidate, parent = self.calculateDepth(tree.right, val)
            if candidate >= 0:
                return candidate + 1, parent
        return -1, None
