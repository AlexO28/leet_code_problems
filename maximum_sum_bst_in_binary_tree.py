# Given a binary tree root, return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).
# Assume a BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional


class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.max_sum = 0
        self.search(root)
        return self.max_sum

    def search(self, node):
        if node is None:
            return 1, float("inf"), float("-inf"), 0
        left_is_bst, left_min, left_max, left_sum = self.search(node.left)
        right_is_bst, right_min, right_max, right_sum = self.search(node.right)
        if left_is_bst and right_is_bst and left_max < node.val < right_min:
            current_sum = left_sum + right_sum + node.val
            self.max_sum = max(self.max_sum, current_sum)
            return (1, min(left_min, node.val), max(right_max, node.val), current_sum)
        return 0, 0, 0, 0
