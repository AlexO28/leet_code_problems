# Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.
# It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.
# A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.
# A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.construct_bst_from_preorder(preorder)

    def construct_bst_from_preorder(self, preorder_values):
        if not preorder_values:
            return None
        else:
            root = TreeNode(preorder_values[0])
            left_index, right_index = 1, len(preorder_values)
            while left_index < right_index:
                mid = (left_index + right_index) // 2
                if preorder_values[mid] > preorder_values[0]:
                    right_index = mid
                else:
                    left_index = mid + 1
            root.left = self.construct_bst_from_preorder(preorder_values[1:left_index])
            root.right = self.construct_bst_from_preorder(preorder_values[left_index:])
            return root
