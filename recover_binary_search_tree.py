# Two values have been swapped in the binary search tree.
# The goal is to recover the binary search tree. Inplace.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, tree):
        res = []
        if tree.left is not None:
            res.extend(self.inorderTraversal(tree.left))
        res.append(tree.val)
        if tree.right is not None:
            res.extend(self.inorderTraversal(tree.right))
        return res

    def arrayToBST(self, arr, tree):
        if tree is not None:     
            self.arrayToBST(arr, tree.left)
            symb = arr.pop(0)
            tree.val = symb
            self.arrayToBST(arr, tree.right)

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = self.inorderTraversal(root)
        arr.sort()
        self.arrayToBST(arr, root)
