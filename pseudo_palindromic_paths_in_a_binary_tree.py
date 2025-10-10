# Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.
# Return the number of pseudo-palindromic paths going from the root node to leaf nodes.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        return self.search(root, 0)

    def search(self, tree, frequency_mask):
        if tree is None:
            return 0
        else:
            frequency_mask ^= 1 << tree.val
            if (tree.left is None) and (tree.right is None):
                return int((frequency_mask & (frequency_mask - 1)) == 0)
            else:
                return self.search(tree.left, frequency_mask) + self.search(
                    tree.right, frequency_mask
                )
