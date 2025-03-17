# Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.
# A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.best_v = 0
        self.findExtremeValues(root)
        return self.best_v

    def findExtremeValues(self, tree):
        if (tree.left is None) and (tree.right is None):
            return tree.val, tree.val
        elif (tree.left is not None) and (tree.right is None):
            min_val, max_val = self.findExtremeValues(tree.left)
            self.best_v = max(self.best_v, abs(tree.val - min_val), abs(tree.val - max_val))
            return min(min_val, tree.val), max(max_val, tree.val)
        elif (tree.left is None) and (tree.right is not None):
            min_val, max_val = self.findExtremeValues(tree.right)
            self.best_v = max(self.best_v, abs(tree.val - min_val), abs(tree.val - max_val))
            return min(min_val, tree.val), max(max_val, tree.val)
        else:
            min_val_1, max_val_1 = self.findExtremeValues(tree.left)
            min_val_2, max_val_2 = self.findExtremeValues(tree.right)
            min_val = min(min_val_1, min_val_2)
            max_val = max(max_val_1, max_val_2)
            self.best_v = max(self.best_v, abs(tree.val - min_val), abs(tree.val - max_val))
            return min(min_val, tree.val), max(max_val, tree.val)
