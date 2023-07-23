# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any non-empty path.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getStatsForTree(self, tree):
        if (tree.left is None) and (tree.right is None):
            return tree.val, tree.val, tree.val
        if (tree.left is not None) and (tree.right is not None):
            stats_left = self.getStatsForTree(tree.left)
            stats_right = self.getStatsForTree(tree.right)
            local_val = max(stats_left[1] + tree.val, stats_right[1] + tree.val, tree.val)
            double_val = stats_left[1] + tree.val + stats_right[1]
            global_val = max(local_val, double_val,
                             stats_left[0], stats_right[0],
                             stats_left[1], stats_right[1],
                             stats_left[2], stats_right[2])
            return global_val, local_val, double_val
        if tree.left is None:
            stats_right = self.getStatsForTree(tree.right)
            local_val = max(stats_right[1] + tree.val, tree.val)
            global_val = max(local_val, stats_right[0], stats_right[1], stats_right[2])
            return global_val, local_val, local_val
        stats_left = self.getStatsForTree(tree.left)
        local_val = max(stats_left[1] + tree.val, tree.val)
        global_val = max(local_val, stats_left[0], stats_left[1], stats_left[2])
        return global_val, local_val, local_val

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        stats = self.getStatsForTree(root)
        return stats[0]
