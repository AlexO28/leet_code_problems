# A maximum tree is a tree where every node has a value greater than any other value in its subtree.
# You are given the root of a maximum binary tree and an integer val.
# Just as in the previous problem, the given tree was constructed from a list a (root = Construct(a)) recursively with the following Construct(a) routine:
# If a is empty, return null.
# Otherwise, let a[i] be the largest element of a. Create a root node with the value a[i].
# The left child of root will be Construct([a[0], a[1], ..., a[i - 1]]).
# The right child of root will be Construct([a[i + 1], a[i + 2], ..., a[a.length - 1]]).
# Return root.
# Note that we were not given a directly, only a root node root = Construct(a).
# Suppose b is a copy of a with the value val appended to it. It is guaranteed that b has unique values.
# Return Construct(b).
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.insert(root, val)

    def insert(self, tree, val):
        if (tree is None) or (tree.val < val):
            return TreeNode(val, tree)
        else:
            tree.right = self.insert(tree.right, val)
            return tree
