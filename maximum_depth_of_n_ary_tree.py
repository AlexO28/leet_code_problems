# Given a n-ary tree, find its maximum depth.

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        return self.findDepth(root)

    def findDepth(self, tree):
        if len(tree.children) == 0:
            return 1
        max_val = 0
        for child in tree.children:
            max_val = max(max_val, self.findDepth(child))
        return 1 + max_val
