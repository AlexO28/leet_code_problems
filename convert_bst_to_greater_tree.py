# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        self.modifyNodes(root, 0)
        return root

    def modifyNodes(self, tree, val_above):
        if tree.right is not None:
            val_right = self.modifyNodes(tree.right, val_above)
            tree.val += val_right
        else:
            tree.val += val_above
        if tree.left is not None:
            return self.modifyNodes(tree.left, tree.val)
        return tree.val
