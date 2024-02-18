# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.findInfoForDiameter(root)[1] - 1

    def findInfoForDiameter(self, tree):
        if (tree.left is None) and (tree.right is None):
            return [1, 1]
        elif (tree.left is None) and (tree.right is not None):
            cur_val, max_val = self.findInfoForDiameter(tree.right)
            return cur_val + 1, max(max_val, cur_val + 1)
        elif (tree.left is not None) and (tree.right is None):
            cur_val, max_val = self.findInfoForDiameter(tree.left)
            return cur_val + 1, max(max_val, cur_val + 1)
        else:
            cur_left, max_left = self.findInfoForDiameter(tree.left)
            cur_right, max_right = self.findInfoForDiameter(tree.right)
            return 1 + max(cur_left, cur_right), max(max_left, max_right, cur_left + cur_right + 1)
