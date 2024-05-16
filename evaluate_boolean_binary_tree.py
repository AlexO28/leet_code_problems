# You are given the root of a full binary tree with the following properties:
# Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
# Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.
# The evaluation of a node is as follows:
# If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
# Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.
# Return the boolean result of evaluating the root node.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return self.evaluate(root)

    def evaluate(self, tree):
        if (tree.val == 0) or (tree.val == 1):
            return bool(tree.val)
        if tree.left is None:
            return self.evaluate(tree.right)
        if tree.right is None:
            return self.evaluate(tree.left)
        left_res = self.evaluate(tree.left)
        right_res = self.evaluate(tree.right)
        if tree.val == 2:
            return left_res or right_res
        else:
            return left_res and right_res
 
