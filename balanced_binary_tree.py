# check if binary tree is balanced

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkBalance(self, tree):
        if tree.left is not None:
            balance_left = self.checkBalance(tree.left)
        else:
            balance_left = [True, 0]
        if tree.right is not None:
            balance_right = self.checkBalance(tree.right)
        else:
            balance_right = [True, 0]
        height = 1 + max(balance_left[1], balance_right[1])
        if abs(balance_right[1] -  balance_left[1]) > 1:
            balance_info = False
        else:
            balance_info = balance_left[0] and balance_right[0]
        return [balance_info, height]

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.checkBalance(root)[0]
