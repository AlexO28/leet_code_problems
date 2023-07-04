# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.


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
        if (tree.left is not None) and (tree.right is not None):
            return min(self.treeSize(tree.left) + 1, self.treeSize(tree.right) + 1)
        if tree.left is not None:
            return self.treeSize(tree.left) + 1
        if tree.right is not None:
            return self.treeSize(tree.right) + 1
        return 1

    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.treeSize(root)
