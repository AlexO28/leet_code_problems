# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def sameTree(p, q):
    if p is None and q is None:
        return True
    elif p is None and q is not None:
        return False
    elif q is None and p is not None:
        return False
    if p.val != q.val:
        return False
    good_lefts = sameTree(p.left, q.left)
    good_rights = sameTree(p.right, q.right)
    return good_lefts and good_rights

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return sameTree(p, q)
