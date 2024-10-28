# Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.
# Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.
# A full binary tree is a binary tree where each node has exactly 0 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import cache


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        return self.buildTree(n)

    @cache
    def buildTree(self, n):
        if n == 1:
            return [TreeNode()]
        else:
            res = []
            for node_left in range(n-1):
                for left_tree in self.buildTree(node_left):
                    for right_tree in self.buildTree(n - node_left - 1):
                        res.append(TreeNode(0, left_tree, right_tree))
            return res
