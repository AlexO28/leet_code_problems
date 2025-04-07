# Given the root of a binary tree and an integer limit, delete all insufficient nodes in the tree simultaneously, and return the root of the resulting binary tree.
# A node is insufficient if every root to leaf path intersecting this node has a sum strictly less than limit.
# A leaf is a node with no children.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        return self.processInsufficientNodes(root, limit)
       

    def processInsufficientNodes(self, tree, limit):
        if tree is None:
            return None
        limit -= tree.val
        if (tree.left is None) and (tree.right is None):
            if limit > 0:
                return None
            else:
                return tree
        tree.left = self.processInsufficientNodes(tree.left, limit)
        tree.right = self.processInsufficientNodes(tree.right, limit)
        if (tree.left is None) and (tree.right is None):
            return None
        else:
            return tree
