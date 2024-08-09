# Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.
# A subtree of a node node is node plus every node that is a descendant of node.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if self.prune(root):
            return None
        else:
            return root

    def prune(self, tree):
        if tree.left is not None:
            safe_to_delete_left = self.prune(tree.left)
            if safe_to_delete_left:
                tree.left = None
        else:
            safe_to_delete_left = True
        if tree.right is not None:
            safe_to_delete_right = self.prune(tree.right)
            if safe_to_delete_right:
                tree.right = None
        else:
            safe_to_delete_right = True
        return (tree.val == 0) & (safe_to_delete_left) & (safe_to_delete_right)
