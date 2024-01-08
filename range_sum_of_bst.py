# Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a value in the inclusive range [low, high].
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return sum(self.BSTtoArray(root, low, high))

    def BSTtoArray(self, tree, low, high):
        if tree is None:
            return []
        if (tree.val >= low) and (tree.val <= high):
            arr = [tree.val]
        else:
            arr = []
        leftVals = self.BSTtoArray(tree.left, low, high)
        rightVals = self.BSTtoArray(tree.right, low, high)
        arr.extend(leftVals)
        arr.extend(rightVals)
        return arr
