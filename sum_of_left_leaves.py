# Given the root of a binary tree, return the sum of all left leaves.
# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.calculateLeftSum(root, left_neighbor=False)

    def calculateLeftSum(self, tree, left_neighbor):
        if (tree.left is None) and (tree.right is None):
            if left_neighbor:
                return tree.val
            else:
                return 0
        elif (tree.left is not None) and (tree.right is not None):
            return self.calculateLeftSum(tree.left, True) + self.calculateLeftSum(tree.right, False)
        elif (tree.left is not None):
            return self.calculateLeftSum(tree.left, True)
        else:
            return self.calculateLeftSum(tree.right, False)
 
