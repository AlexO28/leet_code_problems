# You are given two binary trees root1 and root2.
# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of the new tree.
# Return the merged tree.
# Note: The merging process must start from the root nodes of both trees.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        return self.mergeNonEmptyTrees(root1, root2)

    def mergeNonEmptyTrees(self, tree1, tree2):
        if tree1.left is None:
            tree_left = tree2.left
        elif tree2.left is None:
            tree_left = tree1.left
        else:
            tree_left = self.mergeNonEmptyTrees(tree1.left, tree2.left)
        if tree1.right is None:
            tree_right = tree2.right
        elif tree2.right is None:
            tree_right = tree1.right
        else:
            tree_right = self.mergeNonEmptyTrees(tree1.right, tree2.right)
        return TreeNode(tree1.val + tree2.val, tree_left, tree_right)
