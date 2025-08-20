# Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.
# Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.
# Note that you need to maximize the answer before taking the mod and not after taking it.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.max_product = 0
        modulo_base = 10**9 + 7
        self.total_sum = self.calculate_tree_sum(root)
        self.find_max_product(root)
        return self.max_product % modulo_base

    def calculate_tree_sum(self, node):
        if node is None:
            return 0
        else:
            return (
                node.val
                + self.calculate_tree_sum(node.left)
                + self.calculate_tree_sum(node.right)
            )

    def find_max_product(self, node):
        if node is None:
            return 0
        else:
            current_sum = (
                node.val
                + self.find_max_product(node.left)
                + self.find_max_product(node.right)
            )
            if current_sum < self.total_sum:
                self.max_product = max(
                    self.max_product, current_sum * (self.total_sum - current_sum)
                )
            return current_sum
