# Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = self.inorderTraversal(root)
        res = None
        for elem in arr[::-1]:
            res = TreeNode(elem, None, res)
        return res


    def inorderTraversal(self, tree):
        arr = []
        if tree.left is not None:
            arr = self.inorderTraversal(tree.left)
        arr.append(tree.val)
        if tree.right is not None:
            arr.extend(self.inorderTraversal(tree.right))
        return arr
