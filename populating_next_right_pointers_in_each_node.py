# You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connectVertices(self, vertices):
        kids = []
        hasKids = vertices[0].left is not None
        for j in range(len(vertices)):
            if j>=1:
                vertices[j-1].next = vertices[j]
            if hasKids:
                kids.append(vertices[j].left)
                kids.append(vertices[j].right)
        if hasKids:
            self.connectVertices(kids)

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is not None:
            self.connectVertices([root])
        return root
