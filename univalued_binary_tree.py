# A binary tree is uni-valued if every node in the tree has the same value.
# Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        return self.checkTree(root.left, root.val) and self.checkTree(root.right, root.val)

    def checkTree(self, tree, val):
        if tree is None:
            return True
        if tree.val != val:
            return False
        return self.checkTree(tree.left, val) and self.checkTree(tree.right, val)
 
