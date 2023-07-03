# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def isValid(tree, minVal, maxVal):
    if tree is None:
        return True
    if (tree.val <= minVal) or (tree.val >= maxVal):
        return False
    return isValid(tree.left, minVal, tree.val) and isValid(tree.right, tree.val, maxVal)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return isValid(root, -2**31-1, 2**31)
