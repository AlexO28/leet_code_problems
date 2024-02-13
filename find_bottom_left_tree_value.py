# Given the root of a binary tree, return the leftmost value in the last row of the tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        value, height = self.findValue(root)
        return value

    def findValue(self, tree):
        if (tree.left is None) and (tree.right is None):
            return tree.val, 0
        elif (tree.left is None) and (tree.right is not None):
            value, height = self.findValue(tree.right)
            return value, height+1
        elif (tree.left is not None) and (tree.right is None):
            value, height = self.findValue(tree.left)
            return value, height+1
        else:
            value_left, height_left = self.findValue(tree.left)
            value_right, height_right = self.findValue(tree.right)
            if height_left >= height_right:
                return value_left, height_left+1
            else:
                return value_right, height_right+1
