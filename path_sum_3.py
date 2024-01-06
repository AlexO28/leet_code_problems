# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.
# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).
from collections import Counter

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        path_counts = Counter({0: 1})
        return self.dfs(targetSum, root, 0, path_counts)

    def dfs(self, target_sum, node, current_sum, path_counts):
        if node is None:
            return 0
        current_sum += node.val          
        path_count = path_counts[current_sum - target_sum]
        path_counts[current_sum] += 1
        path_count += self.dfs(target_sum, node.left, current_sum, path_counts)
        path_count += self.dfs(target_sum, node.right, current_sum, path_counts)
        path_counts[current_sum] -= 1          
        return path_count
