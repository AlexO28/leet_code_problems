# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def simultaneousTraverse(self, tree1, tree2):
        if (tree1 is None) and (tree2 is None):
            return True
        if (tree1 is None) and (tree2 is not None):
            return False
        if (tree1 is not None) and (tree2 is None):
            return False
        if tree1.val != tree2.val:
            return False
        if not self.simultaneousTraverse(tree1.left, tree2.right):
            return False
        if not self.simultaneousTraverse(tree1.right, tree2.left):
            return False
        return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.simultaneousTraverse(root.left, root.right)
