# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findAncestor(self, tree, p, q):
        if tree.val == p:
            return tree
        elif tree.val == q:
            return tree
        elif (tree.val < p) and (tree.val < q):
            return self.findAncestor(tree.right, p, q)
        elif (tree.val > p) and (tree.val > q):
            return self.findAncestor(tree.left, p, q)
        elif ((tree.val > p) and (tree.val < q)) or\
             ((tree.val > q) and (tree.val < p)):
            return tree

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.findAncestor(root, p.val, q.val)
