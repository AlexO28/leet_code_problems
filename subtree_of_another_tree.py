# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
# A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.hasSubtree(root, subRoot)

    def hasSubtree(self, tree, subtree):
        if self.areIdentical(tree, subtree):
            return True
        if tree.left is not None:
            if self.hasSubtree(tree.left, subtree):
                return True
        if tree.right is not None:
            if self.hasSubtree(tree.right, subtree):
                return True
        return False

    def areIdentical(self, tree1, tree2):
        if (tree1 is None) and (tree2 is None):
            return True
        elif tree1 is not None:
            if tree2 is None:
                return False
            if tree1.val != tree2.val:
                return False
            if self.areIdentical(tree1.left, tree2.left):
                if self.areIdentical(tree1.right, tree2.right):
                    return True
                else:
                    return False
            else:
                return False
        else:
            if tree2 is not None:
                return False        
        return False
