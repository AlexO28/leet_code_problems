# Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

import numpy as np


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        return self.calculateStatistics(root)[2]

    def calculateStatistics(self, tree):
        if (tree.left is None) and (tree.right is None):
            return tree.val, 1, 1
        elif (tree.left is not None) and (tree.right is not None):
            stats_left = self.calculateStatistics(tree.left)
            stats_right = self.calculateStatistics(tree.right)
            sum_total = stats_left[0] + stats_right[0] + tree.val
            num_total = stats_left[1] + stats_right[1] + 1
            accepted = stats_left[2] + stats_right[2]
            if int(np.floor(sum_total/num_total)) == tree.val:
                return sum_total, num_total, accepted + 1
            else:
                return sum_total, num_total, accepted
        elif tree.right is None:
            stats_left = self.calculateStatistics(tree.left)
            sum_total = stats_left[0] + tree.val
            num_total = stats_left[1] + 1
            accepted = stats_left[2]
            if int(np.floor(sum_total/num_total)) == tree.val:
                return sum_total, num_total, accepted + 1
            else:
                return sum_total, num_total, accepted
        else:
            stats_right = self.calculateStatistics(tree.right)
            sum_total = stats_right[0] + tree.val
            num_total = stats_right[1] + 1
            accepted = stats_right[2]
            if int(np.floor(sum_total/num_total)) == tree.val:
                return sum_total, num_total, accepted + 1
            else:
                return sum_total, num_total, accepted
