# You are given the root of a binary tree.
# A ZigZag path for a binary tree is defined as follow:
# Choose any node in the binary tree and a direction (right or left).
# If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
# Change the direction from right to left or from left to right.
# Repeat the second and third steps until you can't move in the tree.
# Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).
# Return the longest ZigZag path contained in that tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0
        self.search(root, 0, 0)
        return self.max_length

    def search(self, tree, left_length, right_length):
        if tree is not None:
            self.max_length = max(self.max_length, left_length, right_length)
            self.search(tree.left, right_length + 1, 0)
            self.search(tree.right, 0, left_length + 1)
