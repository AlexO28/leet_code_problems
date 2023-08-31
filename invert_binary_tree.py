# Given the root of a binary tree, invert the tree, and return its root.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invert(self, tree):
        if tree.left is not None:
            right_tree = self.invert(tree.left)
        else:
            right_tree = None
        if tree.right is not None:
            left_tree = self.invert(tree.right)
        else:
            left_tree = None
        return TreeNode(tree.val, left_tree, right_tree)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        else:
            return self.invert(root)
