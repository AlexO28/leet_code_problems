# You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.
# For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.
# The test cases are generated so that the answer fits in a 32-bits integer.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        paths = self.findPaths(root)
        return sum([int("".join(path[::-1]), 2) for path in paths])

    def findPaths(self, tree):
        if (tree.left is None):
            res_left = []
        else:
            res_left = self.findPaths(tree.left).copy()
            for j in range(len(res_left)):
                res_left[j].append(str(tree.val))
        if (tree.right is None):
            res_right = []
        else:
            res_right = self.findPaths(tree.right).copy()
            for j in range(len(res_right)):
                res_right[j].append(str(tree.val))
        res_left.extend(res_right)
        if len(res_left) == 0:
            return [[str(tree.val)]]
        else:
            return res_left
