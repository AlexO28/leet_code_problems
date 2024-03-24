# Given the root of an n-ary tree, return the postorder traversal of its nodes' values.
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        return self.postTraversal(root)

    def postTraversal(self, tree):
        res = []
        for child in tree.children:
            arr = self.postTraversal(child)
            res.extend(arr)
        res.append(tree.val)
        return res
