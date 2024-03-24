# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        return self.preorderTraversal(root)

    def preorderTraversal(self, tree):
        res = [tree.val]
        for child in tree.children:
            arr = self.preorderTraversal(child)
            res.extend(arr)
        return res
