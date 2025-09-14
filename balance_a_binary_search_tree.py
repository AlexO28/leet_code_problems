# Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.
# A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional


class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sorted_values = []
        self.inorder_traversal(root)
        return self.build_balanced_bst(0, len(self.sorted_values) - 1)

    def inorder_traversal(self, node):
        if node is None:
            return
        self.inorder_traversal(node.left)
        self.sorted_values.append(node.val)
        self.inorder_traversal(node.right)

    def build_balanced_bst(self, left_idx, right_idx):
        if left_idx > right_idx:
            return None
        mid_idx = (left_idx + right_idx) // 2
        left_subtree = self.build_balanced_bst(left_idx, mid_idx - 1)
        right_subtree = self.build_balanced_bst(mid_idx + 1, right_idx)
        return TreeNode(self.sorted_values[mid_idx], left_subtree, right_subtree)
