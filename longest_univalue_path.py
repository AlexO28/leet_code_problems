# Given the root of a binary tree, return the length of the longest path, where each node in the path has the same value. This path may or may not pass through the root.
# The length of the path between two nodes is represented by the number of edges between them.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.longest_path = 0
        self.search(root)
        return self.longest_path

    def search(self, tree):
        if tree is None:
            return 0
        left_path_length = self.search(tree.left)
        right_path_length = self.search(tree.right)
        left_path = 0
        if tree.left is not None:
            if tree.left.val == tree.val:
                left_path = left_path_length + 1
        right_path = 0
        if tree.right is not None:
            if tree.right.val == tree.val:
                right_path = right_path_length + 1          
        self.longest_path = max(self.longest_path, left_path + right_path)
        return max(left_path, right_path)
