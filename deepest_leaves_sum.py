# Given the root of a binary tree, return the sum of values of its deepest leaves.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        depths = self.calculateDepths(root)
        max_key = max(list(depths.keys()))
        return depths[max_key]

    def calculateDepths(self, tree):
        if (tree.left is None) and (tree.right is None):
            return {0: tree.val}
        elif tree.left is None:
            res_right = self.calculateDepths(tree.right)
            res = {0: tree.val}
            for elem in res_right:
                res[elem + 1] = res_right[elem]
            return res
        elif tree.right is None:
            res_left = self.calculateDepths(tree.left)
            res = {0: tree.val}
            for elem in res_left:
                res[elem + 1] = res_left[elem]
            return res
        else:
            res_left = self.calculateDepths(tree.left)
            res_right = self.calculateDepths(tree.right)
            res = {0: tree.val}
            for elem in res_left:
                res[elem + 1] = res_left[elem]
            for elem in res_right:
                next_elem = elem + 1
                if next_elem in res:
                    res[next_elem] += res_right[elem]
                else:
                    res[next_elem] = res_right[elem]
            return res
