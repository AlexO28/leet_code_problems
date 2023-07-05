# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getPathSums(self, tree):
        if (tree.left is None) and (tree.right is None):
            return [tree.val]
        if tree.left is None:
            res = self.getPathSums(tree.right)
            return [tree.val + r for r in res]
        if tree.right is None:
            res = self.getPathSums(tree.left)
            return [tree.val + r for r in res]
        res = self.getPathSums(tree.left)
        res_alt = self.getPathSums(tree.right)
        res.extend(res_alt)
        return [tree.val + r for r in res]
