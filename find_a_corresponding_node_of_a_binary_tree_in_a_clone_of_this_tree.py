# Given two binary trees original and cloned and given a reference to a node target in the original tree.
# The cloned tree is a copy of the original tree.
# Return a reference to the same node in the cloned tree.
# Note that you are not allowed to change any of the two trees or the target node and the answer must be a reference to a node in the cloned tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import Optional


class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        return self.search(cloned, target.val)

    def search(self, tree, target):
        if tree.val == target:
            return tree
        if tree.left is not None:
            res_left = self.search(tree.left, target)
            if res_left is not None:
                return res_left
        if tree.right is not None:
            res_right = self.search(tree.right, target)
            if res_right is not None:
                return res_right
        return None
