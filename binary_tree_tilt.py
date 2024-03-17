# Given the root of a binary tree, return the sum of every tree node's tilt.
# The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values. If a node does not have a left child, then the sum of the left subtree node values is treated as 0. The rule is similar if the node does not have a right child.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return self.calculateTilt(root)[1]

    def calculateTilt(self, tree):
        if (tree.left is None) and (tree.right is None):
            return tree.val, 0
        elif (tree.left is None) and (tree.right is not None):
            tiltRight = self.calculateTilt(tree.right)
            return tree.val + tiltRight[0], abs(tiltRight[0]) + tiltRight[1]
        elif (tree.left is not None) and (tree.right is None):
            tiltLeft = self.calculateTilt(tree.left)
            return tree.val + tiltLeft[0], abs(tiltLeft[0]) + tiltLeft[1]
        else:
            tiltLeft = self.calculateTilt(tree.left)
            tiltRight = self.calculateTilt(tree.right)
            return tiltLeft[0] + tiltRight[0] + tree.val, abs(tiltLeft[0] - tiltRight[0]) + abs(tiltLeft[1]) + abs(tiltRight[1])
