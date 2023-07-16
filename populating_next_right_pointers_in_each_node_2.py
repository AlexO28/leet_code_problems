# Given a binary tree. Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

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
        for j in range(len(vertices)):
            if j>=1:
                vertices[j-1].next = vertices[j]
            if vertices[j].left is not None:
                kids.append(vertices[j].left)
            if vertices[j].right is not None:
                kids.append(vertices[j].right)
        if len(kids)>0:
            self.connectVertices(kids)

    def connect(self, root: 'Node') -> 'Node':
        if root is not None:
            self.connectVertices([root])
        return root
