# Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. If there are no nodes with an even-valued grandparent, return 0.
# A grandparent of a node is the parent of its parent if it exists.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        self.summa = 0
        self.traverse(root, -1, -1)
        return self.summa

    def traverse(self, tree, parent, grandparent):
        if grandparent % 2 == 0:
            self.summa += tree.val
        if tree.right is not None:
            self.traverse(tree.right, tree.val, parent)
        if tree.left is not None:
            self.traverse(tree.left, tree.val, parent)
