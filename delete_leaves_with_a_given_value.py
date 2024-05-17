# Given a binary tree root and an integer target, delete all the leaf nodes with value target.
# Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if self.pruneTree(root, target):
            return None
        else:
            return root
        
    def pruneTree(self, tree, target):
        if tree.left is not None:
            left_prune = self.pruneTree(tree.left, target)
            if left_prune:
                tree.left = None
        else:
            left_prune = True
        if tree.right is not None:
            right_prune = self.pruneTree(tree.right, target)
            if right_prune:
                tree.right = None
        else:
            right_prune = True
        if left_prune and right_prune:
            if tree.val == target:
                return True
        else:
            return False
