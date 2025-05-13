# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        levels = self.calculateLevelSums(root)
        max_val = max(list(levels.values()))
        keys = list(levels.keys())
        keys.sort()
        for key in keys:
            if levels[key] == max_val:
                return key

    def calculateLevelSums(self, tree):
        levels = {1: tree.val}
        if (tree.left is None) and (tree.right is None):
            return levels
        elif (tree.left is None) and (tree.right is not None):
            levels_right = self.calculateLevelSums(tree.right)
            for level in levels_right:
                levels[level + 1] = levels_right[level]
            return levels
        elif (tree.left is not None) and (tree.right is None):
            levels_left = self.calculateLevelSums(tree.left)
            for level in levels_left:
                levels[level + 1] = levels_left[level]
            return levels
        else:
            levels_left = self.calculateLevelSums(tree.left)
            levels_right = self.calculateLevelSums(tree.right)
            for level in levels_left:
                levels[level + 1] = levels_left[level]
            for level in levels_right:
                next_level = level + 1
                if next_level in levels:
                    levels[next_level] += levels_right[level]
                else:
                    levels[next_level] = levels_right[level]
            return levels
