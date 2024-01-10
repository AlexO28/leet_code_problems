# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.removeNode(root, key)

    def removeNode(self, tree, key):
        if tree is None:
            return None
        if key < tree.val:
            tree.left = self.removeNode(tree.left, key)
            return tree
        if key > tree.val:
            tree.right = self.deleteNode(tree.right, key)
            return tree
        if tree.left is None:
            return tree.right
        if tree.right is None:
            return tree.left
        min_right_subtree = tree.right
        while min_right_subtree.left:
            min_right_subtree = min_right_subtree.left
        tree.val = min_right_subtree.val
        tree.right = self.removeNode(tree.right, min_right_subtree.val)
        return tree
 
