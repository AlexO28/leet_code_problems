# For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.
# A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.
# Given the roots of two binary trees root1 and root2, return true if the two trees are flip equivalent or false otherwise.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.checkFlipEquivalence(root1, root2)


    def checkFlipEquivalence(self, tree1, tree2):
        if (tree1 is None) and (tree2 is not None):
            return False
        if (tree1 is not None) and (tree2 is None):
            return False
        if (tree1 is None) and (tree2 is None):
            return True
        if tree1.val != tree2.val:
            return False
        if (self.checkFlipEquivalence(tree1.left, tree2.left) and self.checkFlipEquivalence(tree1.right, tree2.right)):
            return True
        if (self.checkFlipEquivalence(tree1.right, tree2.left) and self.checkFlipEquivalence(tree1.left, tree2.right)):
            return True
        return False
