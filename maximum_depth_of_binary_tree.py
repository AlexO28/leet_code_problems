# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeSize(self, tree):
        if tree is None:
            return 0
        return max(self.treeSize(tree.left) + 1, self.treeSize(tree.right) + 1)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.treeSize(root)
